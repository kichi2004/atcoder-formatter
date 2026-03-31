from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    error: str | None
    result: str | None
