from pydantic import BaseModel
from typing import Optional, Dict


class MarkdownCreateRequest(BaseModel):
    id: Optional[str]
    title: str
    content: str
    tags: Optional[list]


class MarkdownUpdateRequest(BaseModel):
    tile: Optional[str]
    content: Optional[str]


class MarkdownCreate(BaseModel):
    id: str
    title: str
    content_raw: str
    tags: Optional[Dict[str, list]]  # {"manual": [], "auto": []}
    created_at: str
    updated_at: str
    uploaded_by: str
    visibility: str
    summary: Optional[str]
    sentiment: Optional[str]
