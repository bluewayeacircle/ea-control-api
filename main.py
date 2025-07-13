
from flask import Flask, request, jsonify

app = Flask(__name__)

# Global state
ea_status = {
    "is_running": True,
    "mode": "NORMAL"
}

@app.route("/status", methods=["GET"])
def get_status():
    return jsonify(ea_status)

@app.route("/status", methods=["POST"])
def set_status():
    data = request.get_json()
    if "is_running" in data:
        ea_status["is_running"] = bool(data["is_running"])
    return jsonify(ea_status)

@app.route("/mode", methods=["POST"])
def set_mode():
    data = request.get_json()
    if "mode" in data and data["mode"] in ["NORMAL", "AGGRESSIVE"]:
        ea_status["mode"] = data["mode"]
    return jsonify(ea_status)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
