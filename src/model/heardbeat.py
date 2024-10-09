import json
from helper.time import get_utc_now


class Heardbeat:
    def __init__(self):
        self.event = "Heardbeat"
        self.timestamp = get_utc_now()

    def to_dict(self):
        return {
            "event": self.event,
            "timestamp": self.timestamp,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
