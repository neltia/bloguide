from fastapi import HTTPException, status
from api.common.response_model import ResponseResult
from api.common.result_helper import create_response

import requests


class BlogParserService:
    def __init__(self):
        pass

    """ blog categroy list """
