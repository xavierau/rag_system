from pydantic import BaseModel


class BaseDocument(BaseModel):
    content: str
    meta: dict = {}


class BaseGeneratedResponse(BaseModel):
    content: str
    meta: dict = {}
