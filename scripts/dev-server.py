import http.server
import socketserver
import subprocess
import os
import argparse
import mimetypes

DOCS_DIR = "docs"

class DevServerRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == '/':
            self.run_make_command()
            self.serve_file("index.html")
        elif self.path.startswith('/'):
            file_name = self.path[1:]
            self.run_make_command()
            self.serve_file(file_name)
        else:
            self.send_error(404, "File not found")


    def run_make_command(self):
        try:
            subprocess.run(['make'], check=True)
        except subprocess.CalledProcessError as e:
            self.send_error(500, f"Make command failed: {e}")
            return

    def serve_file(self, file_name):
        file_path = os.path.join(DOCS_DIR, file_name)
        if os.path.exists(file_path) and os.path.isfile(file_path):
            content_type, _ = mimetypes.guess_type(file_path)
            if not content_type:
                content_type = 'application/octet-stream'

            with open(file_path, 'rb') as file:
                self.send_response(200)
                self.send_header("Content-type", content_type)
                self.end_headers()
                self.wfile.write(file.read())
        else:
            self.send_error(404, f"File not found: {file_path}")

def run_server(port):
    with socketserver.TCPServer(("", port), DevServerRequestHandler) as httpd:
        print(f"Serving on port {port}")
        httpd.serve_forever()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Runs the dev server")
    parser.add_argument('--port', type=int, default=8080, help='Port to serve on (default: 8080)')

    args = parser.parse_args()
    run_server(args.port)
