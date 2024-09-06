from flask import Flask
import subprocess

app = Flask(__name__)

def enable_hotspot():
    # Actual implementation to enable mobile hotspot
    # Write your code here
    print("Hotspot enabled")

def discover_peers():
    # Actual implementation to discover peers using Wi-Fi Direct
    # Write your code here
    # This is a placeholder as actual implementation requires platform-specific code
    peers = ["Device1", "Device2"]
    return peers

@app.route('/')
def index():
    return """
    <html>
        <body>
            <h1>Local Music Speaker</h1>
            <button onclick="startHotspot()">Start Hotspot</button>
            <button onclick="discoverPeers()">Discover Peers</button>
            <p id="status">Status: Not Connected</p>
            <script>
                function startHotspot() {
                    fetch('/start_hotspot').then(response => response.text()).then(data => {
                        document.getElementById('status').innerText = data;
                    });
                }

                function discoverPeers() {
                    fetch('/discover_peers').then(response => response.text()).then(data => {
                        document.getElementById('status').innerText = data;
                    });
                }
            </script>
        </body>
    </html>
    """

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