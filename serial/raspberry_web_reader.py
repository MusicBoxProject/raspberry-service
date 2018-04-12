from http.server import BaseHTTPRequestHandler, HTTPServer
import json
import sys

from pirc522 import RFID


def hexlify_uid(uid):
    return ''.join('{:02x}'.format(byte) for byte in uid).upper()


rc522 = RFID()


class ServerHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        error = True
        (error, tag_type) = rc522.request()
        if not error:
            (error, uid) = rc522.anticoll()
            if not error:
                uid = hexlify_uid(uid)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({"uid": uid}).encode('utf-8'))
                return

        self.send_response(404)
        self.send_header('Content-Type', 'application/json')
        self.end_headers()
        self.wfile.write(json.dumps({"error": "No tag found", "uid": None}).encode('utf-8'))


def run(port=8080):
    server_address = ('', port)
    httpd = HTTPServer(server_address, ServerHandler)
    print('Starting httpd on port', port)
    httpd.serve_forever()


if __name__ == "__main__":
    from sys import argv

    if len(argv) == 2:
        run(port=int(argv[1]))
    else:
        run()
