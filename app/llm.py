from google import genai
from dotenv import load_dotenv
import os

load_dotenv()


class LLMService:

    def __init__(self):
        self.client = genai.Client(
            api_key=os.getenv("GEMINI_API_KEY")
        )

    def generate(self, prompt: str) -> str:
        response = self.client.models.generate_content(
            model="gemini-3.5-flash-lite",
            contents=prompt
        )

        return response.text