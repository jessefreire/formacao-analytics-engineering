#!/usr/bin/env python3
"""
Servidor local para visualizar materiais do curso.
Uso: python server.py
"""
import http.server
import socketserver
import webbrowser
import os
import sys

PORT = 8765
DIRECTORY = os.path.dirname(os.path.abspath(__file__))

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=DIRECTORY, **kwargs)
    
    def end_headers(self):
        # Permite fetch dos .md/.txt (CORS local)
        self.send_header('Access-Control-Allow-Origin', '*')
        super().end_headers()
    
    def log_message(self, format, *args):
        # Silencia logs de assets estáticos
        msg = format % args
        if not any(x in msg for x in ('.ico', '.map', '.woff', '.woff2')):
            super().log_message(format, *args)

if __name__ == '__main__':
    os.chdir(DIRECTORY)
    with socketserver.TCPServer(("", PORT), Handler) as httpd:
        url = f"http://localhost:{PORT}"
        print(f"[SERVER] Rodando em {url}")
        print("   Pressione Ctrl+C para parar")
        webbrowser.open(url)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n[SERVER] Encerrado")
            sys.exit(0)