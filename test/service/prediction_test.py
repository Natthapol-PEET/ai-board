from service.prediction import Prediction

model = Prediction()


# item = "can"
item = "bottle"
filename = "test/image/can.jpg"


results = model.process(item, filename)
print(f"results: {results}")
