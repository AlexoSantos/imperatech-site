import http.server
import socketserver
import webbrowser
import os

# Configuração da porta
PORT = 8000

# Garante que o servidor rode no diretório onde este arquivo está
os.chdir(os.path.dirname(os.path.abspath(__file__)))

Handler = http.server.SimpleHTTPRequestHandler

print(f"Iniciando servidor IMPERA em http://localhost:{PORT}")

try:
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        webbrowser.open(f"http://localhost:{PORT}")
        httpd.serve_forever()
except KeyboardInterrupt:
    print("\nServidor encerrado.")