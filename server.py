import socket
import os
from utils import handle_post, read_file


SERVER_HOST = "0.0.0.0"
SERVER_PORT = 8080

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Servidor web escutando na porta {SERVER_PORT}...")

def parse_request(request):
  headers = request.split('\n')
  first_header = headers[0].split()

  http_method = first_header[0]
  path = first_header[1]

  return http_method, path

def get_content_type(path):
  """Return the appropriate content type based on file extension."""
  if path.endswith('.html'):
    return 'text/html'
  elif path.endswith('.css'):
    return 'text/css'
  elif path.endswith('.js'):
    return 'application/javascript'
  else:
    return 'text/plain'

def get_method(path):
  if path == '/':
    path = '/index.html'
  
  if not os.path.splitext(path)[1]:
    path = os.path.join(path, 'index.html')
  
  filepath = path.lstrip('/')

  content = read_file(filepath)
  if content:
    content_type = get_content_type(filepath)
    response = f'HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{content}'
  else:
    response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>'
  
  return response

def post_method(request):
  handle_post(request)
  return f'HTTP/1.1 200 OK\r\n'

def start_server():
  while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(10000).decode()
    http_method, path = parse_request(request)

    if not http_method or not path:
      # Handle malformed request
      response = 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<h1>400 Bad Request</h1>'
    else:
      print(request)
      if http_method == 'GET':
        response = get_method(path)
      elif http_method == 'POST':
        response = post_method(request)

      client_socket.sendall(response.encode())
      client_socket.close()
start_server()
 