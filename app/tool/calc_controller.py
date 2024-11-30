from fastapi import APIRouter
from app.tool import calc_service

router = APIRouter()


@router.post("/date")
async def calculate_date_difference(dates: dict):
    result = calc_service.calculate_date_difference()
    return result


@router.post("/per/total")
async def calculate_percentage(total: dict):
    result = calc_service.calculate_percentage()
    return result


@router.post("/per/increase")
async def calculate_increase(increase_data: dict):
    result = calc_service.calculate_increase()
    return result
