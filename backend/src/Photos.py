import http.server
import socketserver
import os
from werkzeug.wrappers import Request
from werkzeug.datastructures import Headers
from werkzeug.utils import secure_filename

from backend.src.config import SERVER_IP, DATABASE


class MyCustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        path = path.split("/photos/", 1)[-1]
        # Construct the absolute path to the file
        print(os.path.join(DATABASE, "photos", path))
        return os.path.join(DATABASE, "photos", path)

    def do_POST(self):
        headers_list = list(self.headers.items())
        headers = Headers(headers_list)

        environ = {
            "REQUEST_METHOD": "POST",
            "CONTENT_TYPE": headers.get("Content-Type"),
            "wsgi.input": self.rfile,
            "CONTENT_LENGTH": headers.get("Content-Length"),
        }

        request = Request(environ)

        if request.content_type.startswith("multipart/form-data"):
            form = request.files
            if "image" in form:
                image_file = form["image"]
                filename = secure_filename(image_file.filename)
                file_path = os.path.join(DATABASE, "photos", filename)
                image_file.save(file_path)
                self.send_response(200)
                self.send_header("Content-type", "text/plain")
                self.send_header("Access-Control-Allow-Origin", "*")
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
