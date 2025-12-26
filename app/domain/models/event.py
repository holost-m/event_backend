from datetime import datetime
from typing import Literal
from pydantic import BaseModel, Field
from uuid import UUID


class EventCategory(BaseModel):
    id: UUID
    title: str = Field(max_length=32)


class Event(BaseModel):
    id: UUID
    title: str = Field(max_length=64)
    description: str = Field(max_length=512)
    start_dt: datetime
    end_dt: datetime
    location: str = Field(max_length=64)
    event_category: EventCategory
    user: int
    status: Literal["draft", "published", "rejected"]
    created_at: datetime
    published_at: datetime | None


class Subscription(BaseModel):
    id: UUID
    id_user: int
    event_category: EventCategory
