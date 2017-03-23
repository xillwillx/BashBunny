

from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


IS_RUNNING = True


class RequestServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200, "ok")
        self.send_header('Content-type', 'text/plain')
        self.protocol_version = 'HTTP/1.1'

    def do_GET(self):
        self.send_response(200, "ok")
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        try:
            with open(self.path[1:], 'r+') as f:
                data = f.read()
            self.wfile.write(data)
        except IOError:
            self.send_response(404)
            return

    def do_POST(self):
        global IS_RUNNING


        self.send_response(200)
        self.send_header('Access-Control-Allow-Credentials', 'true')
        self.send_header('Access-Control-Allow-Origin', 'http://localhost:8888')
        self.send_header("Content-type", "text/xml")
        self.end_headers()
        content_length = int(self.headers['Content-Length'])

    #    if filename == 'EOF':
    #        IS_RUNNING = False
    #    else:


        data = self.rfile.read(content_length)
        filename = self.path[1:]
        with open("loot/{}.txt".format(filename), "w+") as f:
            f.write(data)
        self._set_headers()


def run(server_class=HTTPServer, handler_class=RequestServer, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    while IS_RUNNING:
        httpd.handle_request()


if __name__ == '__main__':
    run()
