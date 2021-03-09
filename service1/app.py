from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.203.177.146/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


class Win(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    fruit = db.Column(db.String(15))
    prize = db.Column(db.String(50))


@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    names = requests.get("http://35.227.157.65:5001/names")
    fruits = requests.get("http://35.227.157.65:5002/fruits")
    response = requests.post(
        "http://35.227.157.65:5003/prize", data=names.text)
    win = Win(name=names.text, fruit=fruits.text, prize=response.text)
    db.session.add(win)
    db.session.commit()
    return render_template('index.html', names=names.text, fruits=fruits.text, prize=response.text)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
