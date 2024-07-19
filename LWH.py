from http.server import BaseHTTPRequestHandler, HTTPServer

class RequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # Setzt einen Cookie, wenn die URL '/set_cookie' ist
        if self.path == '/set_cookie':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', 'my_cookie=example_value; Path=/')
            self.end_headers()
            self.wfile.write(b'Cookie has been set!')
        
        # Liest und zeigt den Cookie, wenn die URL '/get_cookie' ist
        elif self.path == '/get_cookie':
            cookie_header = self.headers.get('Cookie')
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            if cookie_header:
                self.wfile.write(f'Cookie received: {cookie_header}'.encode())
            else:
                self.wfile.write(b'No cookie found!')
        
        # Löscht den Cookie, wenn die URL '/delete_cookie' ist
        elif self.path == '/delete_cookie':
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.send_header('Set-Cookie', 'my_cookie=; Path=/; expires=Thu, 01 Jan 1970 00:00:00 GMT')
            self.end_headers()
            self.wfile.write(b'Cookie has been deleted!')
        
        else:
            self.send_response(404)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(b'Page not found')

def run(server_class=HTTPServer, handler_class=RequestHandler, port=8080):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print(f'Starting server on port {port}...')
    httpd.serve_forever()

if __name__ == "__main__":
    run()
