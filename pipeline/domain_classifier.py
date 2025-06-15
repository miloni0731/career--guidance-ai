from typing import Dict
from models.generation_model import GenerationModel
from utils.io_helpers import load_config
import json


class DomainClassifier:
    def __init__(self):
        """Initialize the domain classifier."""
        self.model = GenerationModel()
        self.prompt_templates = load_config('prompt_templates')

    def classify(self, preferences: Dict) -> Dict:
        """Map preferences to a career domain using LLM."""
        template = self.prompt_templates['career_mapping']

        # Prepare prompt
        formatted_preferences = json.dumps(preferences, indent=2)
        prompt = self.model.format_prompt(
            system_prompt=template['system'],
            user_prompt=template['user'].format(preferences=formatted_preferences)
        )

        # Call LLM
        response = self.model.generate_text(prompt)

        try:
            # Expecting a dictionary-style JSON from the model
            result = json.loads(response.strip())
            return {
                "career_path": result.get("career_path", "Unknown"),
                "confidence": float(result.get("confidence", 0)),
                "matching_factors": result.get("matching_factors", [])
            }
        except Exception as e:
            print("Failed to parse domain classification response:", e)
            return self._get_default_output()

    def _get_default_output(self) -> Dict:
        """Fallback response when parsing fails."""
        return {
            "career_path": "Undecided",
            "confidence": 0.0,
            "matching_factors": []
        }
