from fastapi import HTTPException, Request
from fastapi.responses import JSONResponse
from http import HTTPStatus
from app.common.response_model import ResponseResult


# HTTPException to ensure responses match the ResponseResult format
async def http_exception_handler(request: Request, exc: HTTPException):
    result_code = exc.status_code
    error_msg = exc.detail if isinstance(exc.detail, str) else HTTPStatus(result_code).phrase
    response = ResponseResult(result_code=result_code, error_msg=error_msg)
    return JSONResponse(status_code=200, content=response.model_dump(exclude_none=True))


# Custom handler for all other exceptions.
async def generic_exception_handler(request: Request, exc: Exception):
    result_code = 500  # Internal Server Error
    error_msg = str(exc)  # Use exception message
    response = ResponseResult(result_code=result_code, error_msg=error_msg)
    return JSONResponse(status_code=result_code, content=response.model_dump(exclude_none=True))
