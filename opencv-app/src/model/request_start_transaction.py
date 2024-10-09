from pydantic import BaseModel, Field
from uuid import UUID
from datetime import datetime


class DataModel(BaseModel):
    type: str = Field(..., pattern=r"^(can|bottle)$")


class RequestStartTransaction(BaseModel):
    id: UUID
    event: str
    data: DataModel
    timestamp: datetime

    class Config:
        json_schema_extra = {
            "example": {
                "id": "82dee7b5-91d5-41b2-bb8e-44c7536605e8",
                "event": "RequestStartTransaction",
                "data": {"type": "can", "serial": "123456"},
                "timestamp": "2024-09-25 08:29:36.949453+00:00",
            }
        }
