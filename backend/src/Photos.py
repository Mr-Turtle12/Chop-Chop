import cgi
import http.server
import socketserver
import os

from backend.src.config import SERVER_IP, DATABASE


class MyCustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split("/photos/", 1)[-1]
        # Construct the absolute path to the file
        print(os.path.join(DATABASE, "photos", path))
        return os.path.join(DATABASE, "photos", path)

    def do_POST(self):
        content_type, _ = cgi.parse_header(self.headers["Content-Type"])
        if content_type == "multipart/form-data":
            form = cgi.FieldStorage(
                fp=self.rfile, headers=self.headers, environ={"REQUEST_METHOD": "POST"}
            )
            if "image" in form:
                image_field = form["image"]
                if image_field.filename:
                    filename = os.path.basename(image_field.filename)
                    file_path = os.path.join(DATABASE, "photos", filename)
                    with open(file_path, "wb") as f:
                        f.write(image_field.file.read())
                    self.send_response(200)
                    self.send_header("Content-type", "text/plain")
                    self.send_header(
                        "Access-Control-Allow-Origin", "http://localhost:8080"
                    )
                    self.end_headers()
                    self.wfile.write(b"Photo saved successfully")
                    return
        # If no image data found or request is not multipart/form-data
        self.send_response(400)
        self.end_headers()
        self.wfile.write(b"Bad request")


def start_http_server():
    PORT = 8000
    Handler = MyCustomHTTPRequestHandler

    with socketserver.TCPServer((SERVER_IP, PORT), Handler) as httpd:
        print(f"HTTP server running at {SERVER_IP}:{PORT}")
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("Server is terminated.")
            httpd.server_close()


if __name__ == "__main__":
    start_http_server()
