from fastapi import APIRouter

from app.services.ai_service import AIService

router = APIRouter(
    prefix="/ai",
    tags=["AI"]
)


@router.get("/test")
def test_ai():

    prompt = """
Say Hello from Gemini AI.
"""

    response = AIService.generate_inventory_analysis(
        prompt
    )

    return {

        "success": True,

        "response": response

    }