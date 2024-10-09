import json
from helper.time import get_utc_now


class AckResponse:
    def __init__(self, id: str, status=True, reason=""):
        self.id = id
        self.status = "Accepted" if status else "Rejected"
        self.reason = reason
        self.timestamp = get_utc_now()

    def to_dict(self):
        return {
            "id": self.id,
            "status": self.status,
            "reason": self.reason,
            "timestamp": self.timestamp,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
