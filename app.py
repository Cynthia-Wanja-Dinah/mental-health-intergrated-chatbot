# render temlate for final document
from email import message
from flask import Flask, jsonify, render_template, request

from chat import get_response


app=Flask(__name__)

@app.get("/")
def index_get():
    return render_template("index.html")


    


@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    respose=get_response(text)
    message={"answear:response"}
    return jsonify(message)


if __name__ == "__main__":
    app.run(debug=True)
