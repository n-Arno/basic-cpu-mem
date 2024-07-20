#!/usr/bin/env python3
import psutil, os

if psutil.LINUX and os.path.exists("/host/proc"):
    psutil.PROCFS_PATH = "/host/proc"

from http.server import HTTPServer, BaseHTTPRequestHandler
from json import dumps
from math import log

def curve(x): 
    # This function is used to give more "variation" to low cpu usage.
    return 100 - 100 * log(100 / (0.9 * x + 10), 10)

def cpu():
    return round(curve(psutil.cpu_percent()),2)

def mem():
    return psutil.virtual_memory().percent

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.sys_version = "Python/3.x"
        self.server_version = "Version/1.0"
        self.send_response(200)
        self.send_header("Content-type", "application/json; charset=utf-8")
        self.end_headers()
        self.wfile.write(dumps({"cpu": cpu(), "mem": mem()}).encode("utf-8"))

    def log_message(self, format, *args):
        return

if __name__ == "__main__":
    httpd = HTTPServer(("0.0.0.0", 80), MyHandler)
    print("Starting server http://0.0.0.0:80", flush=True)
    httpd.serve_forever()
