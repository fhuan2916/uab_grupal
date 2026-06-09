from http.server import HTTPServer, BaseHTTPRequestHandler
class Servidor(BaseHTTPRequestHandler):
    def do_GET(self):
        if self.path =="/":
            with open("index.html", "rb") as archivo:
                self.send_response(200)
                self.send_header("content-type", "text/html")
                self.end_headers()
                self.wfile.write(archivo.read())
        elif self.path =="/estilo.css":
            with open("estilo.css", "rb") as archivo:
                self.send_response(200)
                self.send_header("content-type", "text/css")
                self.end_headers()
                self.wfile.write(archivo.read())

server = HTTPServer(("localhost", 8000), Servidor )
print("Iniciar Servidor")
print("http://localhost:8000")
server.serve_forever()