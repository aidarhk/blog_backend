from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class PostBase(BaseModel):
    title: str
    slug: str
    content_html: str
    category_id: int

class PostCreate(PostBase):
    pass

class PostOut(PostBase):
    id: int
    created_at: datetime
    author_id: int
    
    class Config:
        from_attributes = True
