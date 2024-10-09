# Example input data
from datetime import datetime
from uuid import UUID, uuid4
from model.response_model import ResponseModel


listen_model = ResponseModel(
    id=uuid4(),
    data={"type": "can"},
    timestamp=datetime.now(),
)

dict_output = listen_model.to_dict()
print(f"dict_output:: {dict_output}")

json_output = listen_model.to_json()
print(f"json_output:: {json_output}")
