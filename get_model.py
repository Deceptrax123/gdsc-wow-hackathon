
from keras.models import model_from_json


def saved():
    file = open("model.json", "r")
    loaded = file.read()
    file.close()

    model = model_from_json(loaded)

    return model
