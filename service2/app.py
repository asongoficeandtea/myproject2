from flask import Flask, Response
import random

app = Flask(__name__)


@app.route('/names', methods=['GET'])
def names():
    names = ["leila", "Amina", "maya",
             "Waris", "khadra", "Fatima", "shamhan", "Mariam", "mulki"]
    return Response(random.choice(names), mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
