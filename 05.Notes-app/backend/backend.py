import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

conn = sqlite3.connect("notes.db", check_same_thread=False)
conn.execute("CREATE TABLE IF NOT EXISTS notes (id INTEGER PRIMARY KEY AUTOINCREMENT, text TEXT)")
conn.commit()

class DBHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/add":
            msg = parse_qs(parsed.query).get("msg", [""])[0].strip()
            if msg:
                conn.execute("INSERT INTO notes (text) VALUES (?)", (msg,))
                conn.commit()

        rows = conn.execute("SELECT id, text FROM notes").fetchall()
        data = "\n".join([f"{r[0]}. {r[1]}" for r in rows]) or "Abhi koi note save nahi hai."

        self.send_response(200)
        self.send_header("Content-type", "text/plain; charset=utf-8")
        self.end_headers()
        self.wfile.write(data.encode("utf-8"))

print("Backend DB service port 5000 par ready hai...")
HTTPServer(("0.0.0.0", 5000), DBHandler).serve_forever()
