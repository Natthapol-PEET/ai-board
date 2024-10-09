## AI board

RS232
RS485

Camera 2 ตัว

คุณศิรา

## API Document
- https://docs.google.com/document/d/1DeQcaut1YVdoZgq7VjFcapI0qE1V1XTsouXW-ma72I8/edit#heading=h.a7pj58yfpxak


## Python version
```
Python 3.12.4
```

## Setup env
```
python3 -m venv venv
```

## Activate venv
```
source venv/bin/activate
```

## Install Dependency
```
pip install -r requirements.txt
```

## Run
```
python src/main.py

or

PYTHONPATH=./src python src/main.py
```

## Test
```
PYTHONPATH=./src python test/service/camera_test.py
```

## NanoMQ
```
cd docker
docker-compose -f docker-compose.nanomq.yml up
```

## Install Dependency
```
sudo apt-get install python3-pip

sudo apt-get install python3-opencv

```
