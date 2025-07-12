from flask import Flask, request, jsonify

app = Flask(__name__)

is_running = True
mode = "NORMAL"

@app.route("/status", methods=["GET"])
def status():
    return jsonify({"is_running": is_running, "mode": mode})

@app.route("/trade", methods=["POST"])
def trade():
    data = request.get_json()
    print("TRADE RECEIVED:", data)
    return jsonify({"received": True})

if __name__ == "__main__":
    app.run()
  
