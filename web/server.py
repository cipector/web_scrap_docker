#!/usr/bin/python3
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import json
from socketserver import ThreadingMixIn
import threading
import flats

hostName = "0.0.0.0"
serverPort = 80

class Handler(BaseHTTPRequestHandler):

  def do_GET(self):

      # curl http://<ServerIP>/index.html

      if self.path == "/":
          # spustit flats.py ktery vygeneruje obsah do index.html
          data = flats.get_flats_from_db()
          data["imageurl"] = "<img src=" + data['imageurl'] + ">"
          html_data = data.to_html(escape=False)
          index = f"""<html>
                    <body>{html_data}</body>
                    </html>
          """
          # Respond with the file contents.
          self.send_response(200)
          self.send_header("Content-type", "text/html")
          self.end_headers()
          # content = open('index.html', 'rb').read()
          content = bytes(index, "utf-8")
          # content = index
          self.wfile.write(content)

      else:
          self.send_response(404)

      return

class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
  """Handle requests in a separate thread."""

if __name__ == "__main__":
  webServer = ThreadedHTTPServer((hostName, serverPort), Handler)
  print("Server started http://%s:%s" % (hostName, serverPort))

  try:
      webServer.serve_forever()
  except KeyboardInterrupt:
      pass

  webServer.server_close()
  print("Server stopped.")