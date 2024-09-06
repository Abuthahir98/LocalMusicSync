def setup_ui():
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