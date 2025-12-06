from datetime import datetime
from pydantic import BaseModel, Field
from uuid import UUID


class User(BaseModel):
    id_user: int
    created_at: datetime
    tg_username: str = Field(max_length=64)
    full_name: str = Field(max_length=64)
    last_seen: datetime
    id_role: UUID


class Permission(BaseModel):
    id: UUID
    title: str = Field(max_length=32)
    description: str = Field(max_length=128)


class Role(BaseModel):
    id_role: UUID
    name: str = Field(max_length=32)
    permissions: list[UUID]
