from time import localtime, strftime, sleep

import http.server
import socketserver

PORT = 8000

def currtime():
  return strftime("%Y-%m-%d %H:%M:%S", localtime())

class MyHandler(http.server.BaseHTTPRequestHandler):
  def do_GET(s):
    print('Got request: ' + s.path)
    if s.path == '/time':
      s.send_response(200)
      s.send_header("Content-type", "text/plain")
      s.end_headers()

      body = 'The current time is ' + currtime()
      s.wfile.write(bytes(body, 'utf-8'))
    else:
      s.send_response_only(404)

def main():
  httpd = http.server.HTTPServer(("", PORT), MyHandler)
  print("serving at port", PORT)
  httpd.serve_forever()

if __name__ == '__main__':
  try:
    main()
  except KeyboardInterrupt:
    print('Done')

