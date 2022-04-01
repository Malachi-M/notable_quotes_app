from pydantic import BaseModel

from uuid import UUID, uuid4

class TagBase(BaseModel):
    id: UUID = uuid4()
    name: str

class Tag(TagBase):
    pass

class QuoteBase(BaseModel):
    id: UUID = uuid4()
    author: str | None = None
    content: str
    tags: list[Tag] = []
    source: str

class QuoteRequest(QuoteBase):
    class Config:
        orm_mode = True

class QuoteResponse(QuoteBase):
    class Config:
        orm_mode = True
