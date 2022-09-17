from flask import Flask, jsonify, request
from classifier import  get_pred, get_prediction

app = Flask(__name__)

@app.route("/pred-letter", methods=["POST"])
def predict_data():
  image = request.files.get("alphabet")
  pred = get_pred(image)
  return jsonify({
    "prediction": pred
  }), 200

if __name__ == "__main__":
  app.run(debug=True)