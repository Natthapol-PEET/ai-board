import json
from helper.time import get_utc_now


class TransactionEvent:
    def __init__(self, id: str, status: str, data: dict = {}):
        self.id = id
        self.event = "TransactionEvent"
        self.data = {"status": status}
        self.data.update(data)
        self.timestamp = get_utc_now()

    def to_dict(self):
        return {
            "id": self.id,
            "event": self.event,
            "data": self.data,
            "timestamp": self.timestamp,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
