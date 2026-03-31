from pydantic import BaseModel


class ResponseModel(BaseModel):
    status: str
    error: str | None = None
    result: str | None = None
