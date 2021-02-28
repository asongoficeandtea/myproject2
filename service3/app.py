from flask import Flask, Response
import random

app = Flask(__name__)


@app.route('/fruits', methods=['GET'])
def fruits():
    fruits = ["apple", "orange", "papaya", "grape", "banana", "guava", "kiwi", "mango"]
    return Response(random.choice(fruits), mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5002)
