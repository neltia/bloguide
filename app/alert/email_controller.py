from fastapi import APIRouter
from app.alert import email_service

router = APIRouter()


@router.put("/setting")
async def update_email_settings(settings: dict):
    result = email_service.update_email_settings()
    return result


@router.get("/setting")
async def get_email_settings():
    result = email_service.get_email_settings
    return result


@router.post("/send")
async def send_email(manual_send: dict):
    result = email_service.send_email()
    return result
