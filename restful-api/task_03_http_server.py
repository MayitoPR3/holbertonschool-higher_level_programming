#!/usr/bin/python3
"""API using Python with the `http.server` module"""
from http.server import BaseHTTPRequestHandler, HTTPServer
import json


class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    """class for the Simple HTTP Request Handler"""
    def _set_response(self, status_code=200, content_type='text/plain'):
        """defines the setting of response of the request"""
        self.send_response(status_code)
        self.send_header('Content-type', content_type)
        self.end_headers()

    def do_get(self):
        """method to handle GET requests"""
        if self.path == '/':
            self._set_response()
            self.wfile.write("Hello, this is a simple API!".encode('utf-8'))
        elif self.path == '/data':
            self._set_response(content_type='application/json')
            data = {"name": "John", "age": 30, "city": "New York"}
            self.wfile.write(json.dumps(data).encode('utf-8'))
        elif self.path == '/status':
            self._set_response()
            self.wfile.write("OK".encode('utf-8'))
        else:
            self._set_response(404)
            self.wfile.write("Endpoint not found".encode('utf-8'))


def run(server_class=HTTPServer, handler_class=SimpleHTTPRequestHandler, port=8000):
    """defines the status of the server"""
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f"Server running on port {port}")
    httpd.serve_forever()


if __name__ == '__main__':
    run()
