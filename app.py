from flask import Flask, request, jsonify
from keras.models import model_from_json
import numpy as np
from get_model import saved

model = saved()

app = Flask(__name__)


@app.route("/")
def home():
    return "This is the home page"


@app.route("/predict", methods=["POST"])
def pred():
    data1 = float(request.form['a'])
    data2 = float(request.form['b'])
    data3 = int(request.form['c'])
    data4 = float(request.form['d'])
    data5 = float(request.form['e'])
    data6 = float(request.form['f'])
    data7 = float(request.form['g'])
    data8 = float(request.form['h'])
    data9 = float(request.form['i'])

    arr = np.array(
        [[data1, data2, data3, data4, data5, data6, data7, data8, data9]])
    pred = model.predict(arr)

    pred_list = pred.tolist()
    return jsonify(pred_list)


if __name__ == "__main__":
    app.run(debug=True)
