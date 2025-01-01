from pydantic import BaseModel
from typing import Optional, Any
from http import HTTPStatus


class ResponseResult(BaseModel):
    result_code: int
    result_msg: Optional[str] = None
    error_msg: Optional[str] = None
    data: Optional[Any] = None

    class Config:
        exclude_unset = True
        exclude_none = True

    def __init__(self, **data):
        super().__init__(**data)
        # Set default result_msg based on result_code if not provided
        if not self.result_msg:
            self.result_msg = HTTPStatus(self.result_code).phrase if self.result_code in HTTPStatus._value2member_map_ else "Unknown Status"
