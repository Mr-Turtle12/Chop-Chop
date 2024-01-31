import http.server
import socketserver
import os

from backend.src.config import SERVER_IP, DATABASE


class MyCustomHTTPRequestHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        # Extract the path part after "/photos/"
        path = path.split("/photos/", 1)[-1]
        # Construct the absolute path to the file
        print(os.path.join(DATABASE, "photos", path))
        return os.path.join(DATABASE, "photos", path)


# Start the HTTP server
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


# Start both servers
if __name__ == "__main__":
    start_http_server()
