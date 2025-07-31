from pydantic import BaseModel


class Note(BaseModel):
    no: int
    title: str
    desc: str
    imp: bool = None