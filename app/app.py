import socket
import time
from flask import Flask, request, jsonify

app = Flask(__name__)

def tcp_latency(host, port=443, timeout=3):
    """Return the time (seconds) for a TCP handshake to host:port."""
    start = time.time()
    with socket.create_connection((host, port), timeout=timeout):
        pass
    return time.time() - start

@app.route("/ping")
def ping():
    target = request.args.get("target", "www.google.com")
    try:
        value = tcp_latency(target)
        return jsonify(target=target, latency=value), 200
    except Exception as exc:
        return jsonify(error=str(exc)), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)