from flask import Flask, jsonify
from calculadora import sumar

app = Flask(__name__)

@app.route("/suma/<int:a>/<int:b>")
def suma(a, b):
    return jsonify({"resultado": sumar(a, b)})

if __name__ == "__main__":
    app.run(debug=True)
