#!/usr/bin/env python3

from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
import subprocess
from subprocess import PIPE

class VaultRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        parse_result = urlparse(self.path)
        query_string = parse_result.query
        query_dict = parse_qs(query_string, keep_blank_values=True)
        if 'search' not in query_dict:
            return
        search_string = query_dict['search'][0]
        search_results = self.search_in_vault(search_string)
        self.send_header('Content-type', 'text/html')
        self.end_headers()
        self.wfile.write(bytes(search_results, "utf8"))

    def search_in_vault(self, search_string):
        result = bash("cat ./shellnotes.txt | grep '{}'".format(search_string),
                      stdout=PIPE)
        print("result: ", result)
        result = result.stdout.decode()
        #result.replace('\n', '\r\n')
        print("result: ",result)
        return result

def main():
    run(handler_class=VaultRequestHandler)

def run(server_class=HTTPServer, handler_class=BaseHTTPRequestHandler):
    server_address = ('', 1471)
    httpd = server_class(server_address, handler_class)
    httpd.serve_forever()

def bash(cmd, env=None, source_bashrc=True, stdin=None, stdout=None,
         stderr=None):
    if source_bashrc:
        cmd = "source ~/.bashrc; " + cmd;
    return subprocess.run(cmd, shell=True, executable='/bin/bash', env=env,
                          stdin=stdin, stdout=stdout, stderr=stderr)

if __name__ == "__main__":
    main()
