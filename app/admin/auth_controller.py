from fastapi import APIRouter

router = APIRouter()


@router.post("/{user_id}")
async def create_user_token(user_id: str):
    # JWT 토큰 생성 로직 추가
    token = "generated_token"
    return {"user_id": user_id, "token": token}
