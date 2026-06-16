from model import predict
from flask import Flask, jsonify, render_template, request
app = Flask(__name__)
@app.route("/")
def home():
     return render_template("index.html")
@app.route("/predict",methods=["POST"])
def output():
     data = request.get_json()
     emi = float(data["emi"])
     bhk=float(data["bhk"])
     total_area=float(data["total_area"])
     price_per_ft = float(data["price_per_ft"])
     owner  = data["owner"]
     input = ([[emi,bhk,total_area,price_per_ft,owner]])
     output = predict(input)
     return jsonify({
          "Price": output
     }
     )
if __name__ == "__main__":
    app.run(debug=True)