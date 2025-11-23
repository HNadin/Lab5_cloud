from flask import Flask, request, jsonify
import random
import string

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def generate_password():
    # GET ?len=12
    length = request.args.get("len")

    # POST {"len": 12}
    body = request.get_json(silent=True)

    if not length and isinstance(body, dict):
        length = body.get("len")

    try:
        length = int(length)
    except:
        length = 12

    chars = string.ascii_letters + string.digits
    password = "".join(random.choice(chars) for _ in range(length))

    return jsonify({
        "password": password,
        "length": length
    })


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
