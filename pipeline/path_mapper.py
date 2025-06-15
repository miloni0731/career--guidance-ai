from models.generation_model import GenerationModel
from utils.io_helpers import load_config
import json

class PathMapper:
    def __init__(self):
        """Initialize the path mapper."""
        self.generation_model = GenerationModel()
        self.career_paths = load_config('career_paths')
        self.prompt_templates = load_config('prompt_templates')

    def map_to_career_path(self, preferences):
        # Prepare the prompt for LLM-based classification
        template = self.prompt_templates['career_mapping']
        prompt = self.generation_model.format_prompt(
            template['system'],
            template['user'].format(preferences=preferences)
        )
        response = self.generation_model.generate_text(prompt)
        # Parse the LLM response (should be a JSON or structured string)
        try:
            result = json.loads(response)
            career_path = result.get('career_path', '')
            confidence = float(result.get('confidence', 0.0))
            explanation = result.get('explanation', '')
            follow_up_questions = result.get('follow_up_questions', [])
        except Exception:
            # Fallback: return raw response
            career_path = response.strip()
            confidence = 0.0
            explanation = ''
            follow_up_questions = []
        return {
            "career_path": career_path,
            "confidence": confidence,
            "explanation": explanation,
            "follow_up_questions": follow_up_questions
        }
    
    def _generate_explanation(self, preferences, career_path):
        """Generate explanation for the career recommendation."""
        template = self.prompt_templates['explanation']
        prompt = self.generation_model.format_prompt(
            template['system'],
            template['user'].format(
                career_path=self.career_paths[career_path]['title'],
                preferences=preferences
            )
        )
        
        response = self.generation_model.generate_text(prompt)
        return response.strip()
    
    def _generate_follow_up_questions(self, career_path):
        """Generate follow-up questions about the career path."""
        template = self.prompt_templates['follow_up']
        prompt = self.generation_model.format_prompt(
            template['system'],
            template['user'].format(career_path=self.career_paths[career_path]['title'])
        )
        
        response = self.generation_model.generate_text(prompt)
        try:
            # Extract questions from the response
            questions_start = response.find("Follow-up Questions:")
            if questions_start == -1:
                return self._get_default_questions(career_path)
            
            questions_text = response[questions_start:]
            questions = [q.strip()[2:] for q in questions_text.split("\n") if q.strip().startswith("-")]
            return questions
        except:
            return self._get_default_questions(career_path)
    
    def _get_default_questions(self, career_path):
        """Return default follow-up questions."""
        path_title = self.career_paths[career_path]['title']
        return [
            f"Have you considered exploring {path_title}?",
            f"Would you enjoy working in {path_title}?",
            f"What aspects of {path_title} interest you the most?"
        ] 