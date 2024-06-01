#!/usr/bin/python3
"""API using Python with the `http.server` module"""
import http.server
import json


class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    """class for the Simple HTTP Request Handler"""

    def _set_headers(self, status_code=200, content_type='text/plain'):
        """
        Set HTTP response headers.
        """

        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_GET(self):
        """method to handle GET requests"""
        if self.path == '/':
            self._set_headers()
            self.wfile.write(b'Hello, this is a simple API!')
        elif self.path == '/data':
            self._set_headers(content_type='application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode())
        elif self.path == '/status':
            self._set_headers()
            self.wfile.write(b'OK')
        else:
            self._set_headers(status_code=404, content_type='text/plain')
            self.wfile.write(b'404 Not Found')


def run(server_class=http.server.HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """defines the status of the server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Starting server on port {port}...")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
