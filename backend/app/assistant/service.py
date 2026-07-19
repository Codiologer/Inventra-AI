from google import genai
from app.core.config import GEMINI_MODEL,GEMINI_API_KEY
from app.core.config import settings
from app.assistant.prompts import SYSTEM_PROMPT


client = genai.Client(
    api_key=settings.GEMINI_API_KEY
)


class AssistantService:

    @staticmethod
    def ask(question: str, context: dict):

        prompt = f"""
        {SYSTEM_PROMPT}

        Database Information:

        {context}

        User Question:

        {question}
        """

        response = client.models.generate_content(
            model=GEMINI_MODEL,
            contents=prompt
        )

        return response.text