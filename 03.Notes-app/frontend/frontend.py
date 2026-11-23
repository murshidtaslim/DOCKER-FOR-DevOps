import urllib.request
import urllib.parse
from http.server import BaseHTTPRequestHandler, HTTPServer

BACKEND_URL = "http://db-service:5000"

class WebHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/favicon.ico":
            self.send_response(404)
            self.end_headers()
            return

        parsed = urllib.parse.urlparse(self.path)
        if parsed.path == "/save":
            req_url = f"{BACKEND_URL}/add?{parsed.query}"
        else:
            req_url = BACKEND_URL

        notes_text = urllib.request.urlopen(req_url).read().decode("utf-8")

        html = f"""
        <html>
        <body style="font-family: sans-serif; max-width: 500px; margin: 40px auto;">
            <h2>Docker 2-Tier Notes App</h2>
            <form action="/save" method="get">
                <input type="text" name="msg" placeholder="Naya note likho..." required>
                <button type="submit">Save Note</button>
            </form>
            <h3>Saved Notes (From db-service container):</h3>
            <pre style="background: #f4f4f4; padding: 15px; border-radius: 5px;">{notes_text}</pre>
        </body>
        </html>
        """
        self.send_response(200)
        self.send_header("Content-type", "text/html; charset=utf-8")
        self.end_headers()
        self.wfile.write(html.encode("utf-8"))

print("Frontend web server port 8000 par ready hai...")
HTTPServer(("0.0.0.0", 8000), WebHandler).serve_forever()
