from flask import Flask, Response
import random

app = Flask(__name__)


@app.route('/names', methods=['GET'])
def names():
    names = ["leila", "Amina", "maya",
             "Waris", "khadra", "Fatima", "shamhan", "Mariam", "mulki"]
    rand_name = random.choice(names)
    return Response(rand_name, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5001)
