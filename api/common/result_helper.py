from fastapi.responses import JSONResponse
from api.common.response_model import ResponseResult
from typing import Any
from http import HTTPStatus


def create_response(result_code: int, data: Any = None, result_msg: str = None) -> JSONResponse:
    """
    Create a standardized JSONResponse based on ResponseResult.
    Ensures result_code and HTTP status_code are synchronized.
    """
    if not result_msg:
        result_msg = HTTPStatus(result_code).phrase if result_code in HTTPStatus._value2member_map_ else "Unknown Status"

    response = ResponseResult(result_code=result_code, result_msg=result_msg, data=data)
    return JSONResponse(status_code=200, content=response.model_dump(exclude_none=True))
