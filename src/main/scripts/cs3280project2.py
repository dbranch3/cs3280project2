#!/usr/bin/env python

import http.server

__author__ = 'Darrell Branch'
__version__ = 'Fall 2020'

class IpValidationServer(http.server.BaseHTTPRequestHandler):

    def do_GET(self):
        self.log_message("path: %s", self.path)
        try:
            path = self.path
            self.log_message("resource: %s", path)
            resource = path[1:]
            print(resource)
            if not resource.startswith('operation'):
                self.log_message("resource: %s", path)
                self.send_error(404, 'Resource must begin with: operation')


            start = len('operation') + 1
            query = resource[start:].split('&')
            print(query)

            body = self.process_and_respond(query)
            self.send_response(200)
            self.send_header('Content-Type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes(body, 'UTF-8'))

        except Exception as exception:
            self.send_error(500, str(exception))

    def process_and_respond(self, query):
        '''
        Processes content for valid query.
        Parameters:
        query - the parameters provided to the query
        '''
        body = 'Hello, ' + ' '.join(word.capitalize() for word in query) + '!'
        html = "<!DOCTYPE html><html>"
        html += "<head><title>"
        html += "Response from L13Server"
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
    server = http.server.HTTPServer(server_address, IpValidationServer)
    print('IP Address Validation Server running on port {}; Type <Ctrl-C> to stop server.'.format(PORT))
    server.serve_forever()
