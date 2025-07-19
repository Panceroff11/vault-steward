from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return jsonify({"status": "Vault steward active", "ping": "🟢"})

@app.route("/validate", methods=["POST"])
def validate():
    data = request.json
    if data and data.get("key") == "Phone" and data.get("trigger") == "CommunicationIsKey":
        return jsonify({"response": "✅ Authorized", "unlock": True})
    return jsonify({"response": "❌ Unauthorized", "unlock": False})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
