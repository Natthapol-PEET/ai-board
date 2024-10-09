import json
from helper.time import get_utc_now


class BootNotification:
    def __init__(self, firmware_version: str, model_version: str):
        self.event = "BootNotification"
        self.data = {
            "firmware_version": firmware_version,
            "model_version": model_version,
        }
        self.timestamp = get_utc_now()

    def to_dict(self):
        return {
            "event": self.event,
            "data": self.data,
            "timestamp": self.timestamp,
        }

    def to_json(self):
        return json.dumps(self.to_dict(), indent=4)
