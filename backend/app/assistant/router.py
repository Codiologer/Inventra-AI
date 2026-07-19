from fastapi import APIRouter

router = APIRouter(
    prefix="/assistant",
    tags=["AI Assistant"]
)


@router.get("/health")
def health():

    return {
        "success": True,
        "message": "AI Assistant Ready"
    }