from typing import Optional

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    err: Optional[str]
    result: Optional[str]
