from flask import Flask, request, jsonify
import socket
import time

app = Flask(__name__)


def tcp_latency(host: str, port: int = 443, timeout: int = 3) -> float:
    """
    Measure raw TCP handshake latency to host:port.

    Returns:
        float – elapsed seconds for the three-way handshake.
    Raises:
        Any exception from socket.create_connection (e.g. timeout, DNS error).
    """
    start = time.time()
    with socket.create_connection((host, port), timeout=timeout):
        pass
    return time.time() - start


# ───────────────────────────────────────────────────────────────
# Routes
# ───────────────────────────────────────────────────────────────
@app.route("/latency")
def latency():
    """
    GET /latency?host=example.com&port=443
    """
    host = request.args.get("host", "www.google.com")
    port = int(request.args.get("port", 443))

    try:
        value = tcp_latency(host, port)
        return jsonify(host=host, port=port, latency=value), 200
    except Exception as exc:
        return jsonify(error=str(exc)), 500


@app.route("/ping")  # alias to keep the old path working
def ping():
    return latency()


# ───────────────────────────────────────────────────────────────
# Entrypoint
# ───────────────────────────────────────────────────────────────
if __name__ == "__main__":
    # NOTE: Matches docker run -p 8000:8080 (host:container)
    app.run(host="0.0.0.0", port=8080)