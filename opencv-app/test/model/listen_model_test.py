# Example input data
from model.request_start_transaction import ListenModel


input_data = {
    "id": "82dee7b5-91d5-41b2-bb8e-44c7536605e8",
    "data": {"type": "can"},
    "timestamp": "2024-09-25 08:29:36.949453+00:00",
}

try:
    validated_data = ListenModel(**input_data)
    print("Data is valid!")
    # print(json.dumps(validated_data.dict(), default=str, indent=4))

except Exception as e:
    print(f"Data validation error: {e}")
