import json
from uuid import UUID
from datetime import datetime


class ResponseModel:
    def __init__(self, id: UUID, data: dict, timestamp: datetime):
        self.id = id
        self.data = data
        self.timestamp = timestamp

    def to_dict(self):
        return {
            "id": str(self.id),
            "data": self.data,
            "timestamp": self.timestamp.isoformat(),
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
