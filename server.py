#!/usr/bin/env python
# -*- coding: utf-8 -*-
import http.server
import socketserver
import os

# 現在のディレクトリを設定
os.chdir(os.path.dirname(os.path.abspath(__file__)))

PORT = 8000

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"サーバーが起動しました！")
    print(f"ブラウザで http://localhost:{PORT} にアクセスしてください")
    print("停止するには Ctrl+C を押してください")
    httpd.serve_forever()
