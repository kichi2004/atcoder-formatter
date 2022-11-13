from typing import Optional

from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    error: Optional[str]
    result: Optional[str]
