from time import localtime, strftime

def currtime():
  return strftime("%Y-%m-%d %H:%M:%S", localtime())

def handle_GET(s):
  s.send_response(200)
  s.send_header("Content-type", "text/plain")
  s.end_headers()

  body = currtime()
  s.wfile.write(bytes(body, 'utf-8'))

