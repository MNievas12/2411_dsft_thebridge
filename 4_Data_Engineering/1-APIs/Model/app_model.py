from flask import Flask, request, jsonify
import pickle

app = Flask(__name__)
app.config["DEBUG"] = True

# Cargar el modelo una sola vez al iniciar la app
with open("./ejercicio/data/advertising_model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

@app.route("/", methods=["GET"])
def home():
    return "Bienvenido a mi API del modelo advertising"

@app.route("/v1/predict", methods=["GET"])
def predict():
    try:
        tv = float(request.args["tv"])
        radio = float(request.args["radio"])
        newspaper = float(request.args["newspaper"])
    except:
        return jsonify({"error": "Missing or invalid parameters. Provide tv, radio, and newspaper as numbers."}), 400

    prediction = model.predict([[tv, radio, newspaper]])[0]
    return jsonify({"prediction": round(prediction, 2)})

if __name__ == "__main__":
    app.run()
