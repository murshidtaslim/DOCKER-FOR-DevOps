from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/plain")
        self.end_headers()
        self.wfile.write(b"Connection Successful! Yeh data my-server container se aaya hai.")

print("Server port 5000 par start ho gaya hai...")
HTTPServer(("0.0.0.0", 5000), MyHandler).serve_forever()
