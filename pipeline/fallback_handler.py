from models.generation_model import GenerationModel
from utils.io_helpers import load_config

class FallbackHandler:
    def __init__(self):
        """Initialize the fallback handler."""
        self.model = GenerationModel()
        self.prompt_templates = load_config('prompt_templates')

    def needs_clarification(self, preferences, confidence):
        """Determine if clarification is needed based on missing preferences or low confidence."""
        if not any([preferences["interests"], preferences["skills"], preferences["traits"]]):
            return True
        if confidence < 0.7:
            return True
        return False

    def get_clarification_questions(self, text):
        """Generate clarifying questions if user input is ambiguous."""
        template = self.prompt_templates["clarification_questions"]
        prompt = self.model.format_prompt(
            system_prompt=template["system"],
            user_prompt=template["user"].format(text=text)
        )

        response = self.model.generate_text(prompt)

        try:
            # Expect JSON-style list output (e.g., ["question1", "question2"])
            questions = eval(response.strip())
            if isinstance(questions, list):
                return [q.strip() for q in questions]
            return self._get_default_questions()
        except:
            return self._get_default_questions()

    def generate_follow_up(self, career_path):
        """Generate follow-up questions to explore the recommended career path."""
        template = self.prompt_templates["follow_up"]
        prompt = self.model.format_prompt(
            system_prompt=template["system"],
            user_prompt=template["user"].format(career_path=career_path)
        )

        response = self.model.generate_text(prompt)

        try:
            # Parse output like:
            # Follow-up Questions:
            # - question 1
            # - question 2
            questions = [line.strip()[2:].strip() for line in response.split("\n")
                         if line.strip().startswith("-")]
            return questions if questions else self._get_default_followups()
        except:
            return self._get_default_followups()

    def _get_default_questions(self):
        """Fallback clarification questions."""
        return [
            "Can you tell me more about what excites you day to day?",
            "Are there any activities you dislike doing?",
            "Do you prefer working with people, data, or ideas?"
        ]

    def _get_default_followups(self):
        """Fallback follow-up questions for exploring career path."""
        return [
            "What type of roles within this field interest you the most?",
            "Would you be open to learning new skills required for this career?",
            "What are your expectations regarding work-life balance in this field?"
        ]
