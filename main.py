from flask import Flask, request, jsonify

app = Flask(__name__)

# Default EA settings
app.config['EA_RUNNING'] = True
app.config['EA_MODE'] = "NORMAL"  # Options: "NORMAL", "AGGRESSIVE"

@app.route('/')
def home():
    return "EA Control API is live!"

@app.route('/status', methods=['GET'])
def get_status():
    return jsonify({
        "is_running": app.config['EA_RUNNING'],
        "mode": app.config['EA_MODE']
    })

@app.route('/status', methods=['POST'])
def set_status():
    if not request.is_json:
        return jsonify({"error": "Expected JSON with Content-Type: application/json"}), 415

    data = request.get_json()
    is_running = data.get('is_running')

    if is_running is None:
        return jsonify({"error": "Missing 'is_running' key"}), 400

    app.config['EA_RUNNING'] = bool(is_running)
    return jsonify({
        "is_running": app.config['EA_RUNNING'],
        "mode": app.config.get("EA_MODE", "NORMAL")
    })

@app.route('/mode', methods=['POST'])
def set_mode():
    if not request.is_json:
        return jsonify({"error": "Expected JSON with Content-Type: application/json"}), 415

    data = request.get_json()
    mode = data.get('mode')

    if mode not in ['NORMAL', 'AGGRESSIVE']:
        return jsonify({"error": "Invalid mode, use 'NORMAL' or 'AGGRESSIVE'"}), 400

    app.config['EA_MODE'] = mode
    return jsonify({
        "is_running": app.config.get("EA_RUNNING", False),
        "mode": app.config['EA_MODE']
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
