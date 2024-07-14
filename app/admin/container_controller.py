from fastapi import APIRouter, HTTPException
from app.admin import container_service

router = APIRouter()


@router.get("/list")
async def get_container_list():
    result = container_service.get_container_list()
    return result


@router.get("/{container_id}")
async def get_container(container_id: str):
    if container_id not in ["container1", "container2"]:
        raise HTTPException(status_code=404, detail="Container not found")
    result = container_service.get_container(container_id)
    return result


@router.post("/{container_id}")
async def create_or_restart_container(container_id: str):
    result = container_service.create_or_restart_container(container_id)
    return result


@router.delete("/{container_id}")
async def delete_container(container_id: str):
    result = container_service.delete_container(container_id)
    return result
