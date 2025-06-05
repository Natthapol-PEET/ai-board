from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def greeting():
    return {"message": "Hello World"}

    # item = "can"
    # filename = "can.jpg"

    # if Globals.objectType == "bottle":
    #     item = "bottle"
    #     filename = "bottle.jpg"

    # prediction_local_results = model.process(item, filename)
    # LogFlight.info(f"prediction_local_results: {prediction_local_results}")
