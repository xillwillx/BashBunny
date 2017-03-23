from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer


IS_RUNNING = True


class RequestServer(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        try:    
            with open(self.path[1:], 'r+') as f:
                data = f.read()
            self.wfile.write(data)
        except IOError:
            self.send_response(404)
            return
        self._set_headers()

    def do_POST(self):
        global IS_RUNNING

        content_length = int(self.headers['Content-Length'])
        data = self.rfile.read(content_length)
        filename = self.path[1:]
        
        with open("{}.txt".format(filename), "w+") as f:
            f.write(data)

        IS_RUNNING = False
        self._set_headers()
       

def run(server_class=HTTPServer, handler_class=RequestServer, port=80):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)

    while IS_RUNNING:
        httpd.handle_request()


if __name__ == '__main__':
    run()
