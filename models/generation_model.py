import streamlit as st
import requests


class GenerationModel:
    def __init__(self):
        self.model_name = st.secrets["api"]["model_name"]
        self.api_token = st.secrets["api"]["hf_token"]
        self.provider = st.secrets["api"].get("provider", "Featherless")
        self.api_url = "https://router.huggingface.co/featherless-ai/v1/chat/completions"
        self.headers = {
            "Authorization": f"Bearer {self.api_token}",
            "Content-Type": "application/json"
        }

    def generate_text(self, prompt: str, max_length: int = 512, temperature: float = 0.7) -> str:
        """Call Featherless AI Chat API using OpenAI-style payload."""
        payload = {
            "model": self.model_name,
            "messages": [
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            "max_tokens": max_length,
            "temperature": temperature
        }

        try:
            response = requests.post(self.api_url, headers=self.headers, json=payload)
            response.raise_for_status()
            result = response.json()

            return result["choices"][0]["message"]["content"]  # Featherless returns OpenAI-like structure

        except requests.HTTPError as e:
            st.error(f"❌ LLM API Error: {response.status_code} — {response.text}")
            return "Error: LLM request failed."
        except Exception as e:
            st.error(f"❌ Unexpected Error: {e}")
            return "Error: Unexpected failure during LLM response."

    def format_prompt(self, system_prompt: str, user_prompt: str) -> str:
        """Format prompt as simple user instructions."""
        return f"{system_prompt.strip()}\n\n{user_prompt.strip()}"
