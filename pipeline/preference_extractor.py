from typing import List, Dict
from models.generation_model import GenerationModel
from utils.io_helpers import load_config


class PreferenceExtractor:
    def __init__(self):
        """Initialize the preference extractor."""
        self.model = GenerationModel()
        self.prompt_templates = load_config('prompt_templates')

    def extract_preferences(self, text: str) -> Dict:
        """Extract preferences from input text using LLM."""
        template = self.prompt_templates['preference_extraction']
        prompt = self.model.format_prompt(
            system_prompt=template['system'],
            user_prompt=template['user'].format(text=text)
        )

        response = self.model.generate_text(prompt)

        try:
            profile_start = response.find("Extracted Profile:")
            if profile_start == -1:
                return self._get_empty_preferences()

            profile_text = response[profile_start:]

            # Extract Interests
            interests_start = profile_text.find("Interests:") + len("Interests:")
            interests_end = profile_text.find("Skills:")
            interests = [i.strip() for i in profile_text[interests_start:interests_end].strip().split(",")]

            # Extract Skills
            skills_start = profile_text.find("Skills:") + len("Skills:")
            skills_end = profile_text.find("Traits:")
            skills = [s.strip() for s in profile_text[skills_start:skills_end].strip().split(",")]

            # Extract Traits
            traits_start = profile_text.find("Traits:") + len("Traits:")
            traits_end = profile_text.find("\n", traits_start)
            if traits_end == -1:
                traits_end = len(profile_text)
            traits = [t.strip() for t in profile_text[traits_start:traits_end].strip().split(",")]

            return {
                "interests": interests,
                "skills": skills,
                "traits": traits,
                "dislikes": []  # Extend if you later extract dislikes explicitly
            }

        except Exception as e:
            print("⚠️ Parsing failed:", e)
            return self._get_empty_preferences()

    def get_clarification_questions(self, text: str) -> List[str]:
        """Generate clarifying questions for ambiguous input."""
        template = self.prompt_templates['clarification_questions']
        prompt = self.model.format_prompt(
            system_prompt=template['system'],
            user_prompt=template['user'].format(text=text)
        )

        response = self.model.generate_text(prompt)

        try:
            # Expecting JSON array from prompt
            questions = eval(response.strip())  # Use json.loads if you're sure it's a valid JSON array
            if isinstance(questions, list):
                return [q.strip() for q in questions]
            return self._get_default_questions()
        except Exception as e:
            print("⚠️ Clarification question parsing failed:", e)
            return self._get_default_questions()

    def _get_empty_preferences(self) -> Dict:
        """Return default empty preferences structure."""
        return {
            "interests": [],
            "skills": [],
            "traits": [],
            "dislikes": []
        }

    def _get_default_questions(self) -> List[str]:
        """Return generic backup clarifying questions."""
        return [
            "Can you describe what kind of tasks or activities you enjoy?",
            "What are some things you dislike doing or avoid?",
            "Are there any fields or subjects that excite you?"
        ]
