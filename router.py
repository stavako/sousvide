#!/usr/bin/python3

import http.server

import timeserver
import fileserver

PORT = 8000

class Router(http.server.BaseHTTPRequestHandler):
  def do_GET(s):
    print('Got request: ' + s.path)
    if s.path == '/api/time':
      timeserver.handle_GET(s)
    else:
      fileserver.handle_GET(s)

def main():
  httpd = http.server.HTTPServer(("", PORT), Router)
  print("serving at port", PORT)
  httpd.serve_forever()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Done')

