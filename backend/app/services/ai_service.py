from google import genai
import traceback

from app.core.config import GEMINI_API_KEY, GEMINI_MODEL


class AIService:

    @staticmethod
    def generate_inventory_analysis(prompt: str):

        try:

            print("=" * 50)
            print("MODEL:", GEMINI_MODEL)
            print("=" * 50)

            client = genai.Client(
                api_key=GEMINI_API_KEY
            )

            response = client.models.generate_content(
                model=GEMINI_MODEL,
                contents=prompt
            )

            return response.text

        except Exception as e:

            print("\nAI ERROR\n")
            traceback.print_exc()

            return str(e)