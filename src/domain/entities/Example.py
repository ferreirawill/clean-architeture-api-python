from pydantic import BaseModel


class Example(BaseModel):
    value: float
    name: str
