import http.server

import timeserver

PORT = 8000

class Router(http.server.BaseHTTPRequestHandler):
  def do_GET(s):
    print('Got request: ' + s.path)
    if s.path == '/time':
      timeserver.handle_GET(s)
    elif s.path == '/':
      with open('index.html', 'r') as f:
        s.send_response(200)
        s.send_header("Content-type", "text/html")
        s.end_headers()

        body = f.read()
        s.wfile.write(bytes(body, 'utf-8'))
    else:
      s.send_response_only(404)

def main():
  httpd = http.server.HTTPServer(("", PORT), Router)
  print("serving at port", PORT)
  httpd.serve_forever()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Done')

