from typing import Dict
from models.generation_model import GenerationModel
from utils.io_helpers import load_config


class ExplanationGenerator:
    def __init__(self):
        """Initialize the explanation generator."""
        self.model = GenerationModel()
        self.prompt_templates = load_config('prompt_templates')

    def generate(self, career_path: str, preferences: Dict) -> str:
        """Generate a personalized explanation for the recommended career path."""
        template = self.prompt_templates['explanation']

        # Prepare formatted prompt
        formatted_preferences = self._format_preferences(preferences)
        prompt = self.model.format_prompt(
            system_prompt=template['system'],
            user_prompt=template['user'].format(
                career_path=career_path,
                preferences=formatted_preferences
            )
        )

        response = self.model.generate_text(prompt)

        try:
            # Strip and validate output
            if response.lower().startswith("explanation:"):
                return response.strip()
            return "Explanation: " + response.strip()
        except Exception as e:
            print("⚠️ Explanation generation failed:", e)
            return "Explanation: This career path aligns well with your overall preferences."

    def _format_preferences(self, prefs: Dict) -> str:
        """Turn dict of preferences into readable sentence for LLM."""
        parts = []
        if prefs.get("interests"):
            parts.append(f"interests: {', '.join(prefs['interests'])}")
        if prefs.get("skills"):
            parts.append(f"skills: {', '.join(prefs['skills'])}")
        if prefs.get("traits"):
            parts.append(f"traits: {', '.join(prefs['traits'])}")
        if prefs.get("dislikes"):
            parts.append(f"dislikes: {', '.join(prefs['dislikes'])}")
        return "; ".join(parts)
