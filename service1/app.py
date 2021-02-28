from flask import Flask, render_template, jsonify, request
from flask_sqlalchemy import SQLAlchemy
import requests
import random

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://alimatea7:root@localhost/flaskdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class Win(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(15))
    fruit = db.Column(db.String(15))
    prize = db.Column(db.String(50))



@app.route('/', methods=["GET"])
@app.route('/index', methods=["GET"])
def index():
    names = requests.get("http://localhost:5001/names")
    fruits = requests.get("http://localhost:5002/fruits")
    account = names.text + fruits.text
    response = requests.post("http://localhost:5003/prize", data=account)

    names1 = names.text
    fruits1 = fruits.text
    prize = response.text
    win = Win(name=names.text, fruit=fruits.text, prize=prize)
    db.session.add(win)
    db.session.commit()
    return render_template('index.html', names1=names, fruits1=fruits,  prize=prize)


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
