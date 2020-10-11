#!/usr/bin/env python

import http.server

from utils import ip_and_subnet_are_valid, get_network_address

__author__ = 'Darrell Branch'
__version__ = 'Fall 2020'

class NetAddressServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            if not resource.startswith('subnet'):
                self.log_message("resource: %s", path)
                self.send_error(404, 'Resource must begin with: subnet')


            start = len('subnet') + 1
            query = resource[start:].split('&')

            inputIsValid = ip_and_subnet_are_valid(query)

            if not inputIsValid:
                self.bad_request("Invalid IP Address or Subnet Mask")

            body = self.process_and_respond(query)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))

        except Exception as exception:
            self.send_error(500, str(exception))

    def bad_request(self, message):
        self.send_error(400, message)          

    def process_and_respond(self, query):
        networkAddress = get_network_address(query)
        body = 'Network Address:     ' + networkAddress
        html = "<!DOCTYPE html><html>"
        html += "<head><title>"
        html += "Response from Network Address Calculator"
        html += "</title></head>"
        html += "<body><p><h1>"
        html += body
        html += "</h1></p></body>"
        html += "</html>"
        self.log_message("page built")
        return html


if __name__ == '__main__':
    PORT = 3280
    server_address = ('', PORT)
    server = http.server.HTTPServer(server_address, NetAddressServer)
    print('Network Address Calculator running on port {}; Type <Ctrl-C> to stop server.'.format(PORT))
    server.serve_forever()
