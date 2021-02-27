from flask import Flask, Response, request
import random

app = Flask(__name__)

cars = ["Porsche 911", "McLaren 570S", "Alpine A110", "Nissan GT-R", "Jaguar F-Type",
        "Mercedes-AMG GT", "Chevrolet Corvette C8", "Lotus Evora", "Audi TT RS", "Lexus LC"]

perfumes = ["Roberto Cavalli Oud al-Qasr", "Black Phantom by Kilian", "Versace Bright Crystal", "Gucci Guilty", "Byredo Gypsy Water", "Maison Francis Kurkdjian Baccarat Rouge 540",
            "Maison Margiela Replica By the Fire", "Jo Malone London Velvet Rose and Oud", "Kay Ali Vanilla 28", "Kilian Rolling in Love"]


@app.route('/prize', methods=["POST"])
def prize():
    full_info = request.get_json()
    names = full_info["names"]
    fruits = full_info["fruits"]

    account = names + fruits
    if account[0].isupper():
        prize = random.choice(perfumes)
    elif account[0].islower():
        prize = random.choice(cars)

    return Response(prize, mimetype='text/plain')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5003)
