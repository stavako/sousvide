import os.path as path
import mimetypes

sourcedir = 'assets'

mimetypes.init()

def handle_GET(s):
  if s.path[0:1] != '/':
    s.send_response_only(404)
    return

  if s.path == '/':
    filepath = 'index.html'
  else: 
    filepath = s.path[1:]

    if '/' in filepath:
      s.send_response_only(404)
      return

  filepath = sourcedir + '/' + filepath

  if not path.exists(filepath):
    s.send_response_only(404)
    return

  mimetype = mimetypes.guess_type(filepath)[0] or "text/plain"

  with open(filepath, 'r') as f:
    s.send_response(200)
    s.send_header("Content-type", mimetype)
    s.end_headers()

    body = f.read()
    s.wfile.write(bytes(body, 'utf-8'))

