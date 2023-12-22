from fastapi import APIRouter


router = APIRouter()


@router.get("/")
async def webhook_handler() -> None:
    return "I am webhook_handler."


@router.on_event("startup")
async def set_webhook() -> None:
    pass