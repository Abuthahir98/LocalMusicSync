from flask import Flask
from app.ui import setup_ui
from app.hotspot import enable_hotspot
from app.wifi_direct import discover_peers

app = Flask(__name__)

@app.route('/')
def index():
    return setup_ui()

@app.route('/start_hotspot')
def start_hotspot():
    enable_hotspot()
    return "Hotspot started"

@app.route('/discover_peers')
def discover_peers_route():
    peers = discover_peers()
    return f"Discovered peers: {peers}"

if __name__ == '__main__':
    app.run(debug=True)