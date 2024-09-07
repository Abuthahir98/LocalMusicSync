from flask import Flask
import subprocess
import time

app = Flask(__name__)

def enable_hotspot():
    """
    Enables the mobile hotspot using nmcli (NetworkManager CLI).
    This example assumes you are using Linux with NetworkManager installed.
    """
    try:
        # Turn on Wi-Fi
        subprocess.run(['nmcli', 'radio', 'wifi', 'on'], check=True)
        
        # Create a hotspot with the specified SSID and password
        subprocess.run([
            'nmcli', 'device', 'wifi', 'hotspot', 
            'ifname', 'wlan0',  # Change 'wlan0' to your Wi-Fi interface name if different
            'ssid', 'MyHotspot', 
            'password', 'mypassword'
        ], check=True)
        
        print("Hotspot enabled successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Failed to enable hotspot: {e}")
        return False
    
    return True

def discover_peers():
    """
    Discovers nearby devices using Wi-Fi Direct.
    This function scans for nearby devices and returns a list of device names (or MAC addresses).
    """
    try:
        # Scan for Wi-Fi Direct peers
        result = subprocess.run(['iw', 'dev', 'wlan0', 'scan'], capture_output=True, text=True, check=True)
        
        # Placeholder logic to parse scan results and find peers
        peers = []
        for line in result.stdout.splitlines():
            if "SSID" in line:
                peers.append(line.split(":")[1].strip())
        
        if not peers:
            peers = ["No devices found"]
        
        print(f"Discovered peers: {peers}")
        return peers
    
    except subprocess.CalledProcessError as e:
        print(f"Failed to discover peers: {e}")
        return ["Error in discovering peers"]

@app.route('/')
def index():
    return """
    <html>
        <body>
            <h1>Local Music Speaker</h1>
            <button onclick="startHotspot()">Start Hotspot</button>
            <button onclick="discoverPeers()">Discover Peers</button>
            <p id="status">Status: Not Connected</p>
            <p id="peers"></p>
            <script>
                function startHotspot() {
                    fetch('/start_hotspot').then(response => response.text()).then(data => {
                        document.getElementById('status').innerText = data;
                    });
                }

                function discoverPeers() {
                    fetch('/discover_peers').then(response => response.text()).then(data => {
                        document.getElementById('peers').innerText = data;
                    });
                }
            </script>
        </body>
    </html>
    """

@app.route('/start_hotspot')
def start_hotspot():
    if enable_hotspot():
        return "Hotspot started successfully."
    else:
        return "Failed to start hotspot."

@app.route('/discover_peers')
def discover_peers_route():
    peers = discover_peers()
    return f"Discovered peers: {', '.join(peers)}"

if __name__ == '__main__':
    app.run(debug=True)
