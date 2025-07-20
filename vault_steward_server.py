from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"ping": "✅", "status": "Vault steward active"})

@app.route("/validate", methods=["POST"])
def validate():
    data = request.get_json()

    if not data or "key" not in data:
        return jsonify({"response": "Error: No key provided."}), 400

    key = data["key"].strip().lower()

    # Accepted keys and responses
    responses = {
        "findtheloneaortatree": "Correct. Anchor 5: Segin Tree unlocked.",
        "tenfeetontherailroad": "Correct. Anchor 2: Vault Radius acquired.",
        "revealthenote": "Correct. Scroll unlocked. Read with care.",
        "communicationiskey": "Confirmed. Channel open."
    }

    if key in responses:
        return jsonify({"response": responses[key]}), 200
    else:
        return jsonify({"response": "Incorrect. Try again."}), 401

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)