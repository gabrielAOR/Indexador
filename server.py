import socket
import re
import os
from utils import handle_post, read_file, find_first_html_file


SERVER_HOST = "0.0.0.0" # need to change to server ip
SERVER_PORT = 8080
client_folders = {}

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
server_socket.bind((SERVER_HOST, SERVER_PORT))
server_socket.listen(5)

print(f"Servidor web escutando na porta {SERVER_PORT}...")

def parse_request(request):
    headers = request.splitlines()
    if not headers:
        return None, None
    first_header = headers[0].split()
    if len(first_header) < 2:
        return None, None
    http_method = first_header[0]
    path = first_header[1]
    return http_method, path

def get_content_type(path):
  if path.endswith('.html'):
    return 'text/html'
  elif path.endswith('.css'):
    return 'text/css'
  elif path.endswith('.js'):
    return 'application/javascript'
  else:
    return 'text/plain'

def get_method(path, client_addr):
  files_pattern = re.compile(r"\.(html|css|js)$")
  ip = client_addr[0]
  base_folder=''

  if ip in client_folders: base_folder = client_folders[ip]

  if files_pattern.search(path): filepath = base_folder + path
  else:
    if os.path.exists(os.getcwd() + path):
      client_folders[ip] = path
      filepath = path +  "/" + find_first_html_file(path.lstrip('/'))
    else:
      return 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>'
  
  content = read_file(filepath.lstrip('/'))
  if content:
    content_type = get_content_type(filepath)
    response = f'HTTP/1.1 200 OK\r\nContent-Type: {content_type}\r\n\r\n{content}'
  else:
    response = 'HTTP/1.1 404 Not Found\r\nContent-Type: text/html\r\n\r\n<h1>404 Not Found</h1>'
  
  return response

def post_method(request):
  handle_post(request)
  response = 'HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\n\r\n'
  return response

def start_server():
  while True:
    client_socket, client_address = server_socket.accept()
    request = client_socket.recv(10000).decode()
    http_method, path = parse_request(request)

    if not http_method or not path:
      response = 'HTTP/1.1 400 Bad Request\r\nContent-Type: text/html\r\n\r\n<h1>400 Bad Request</h1>'
    else:
      print(request)
      if http_method == 'GET':
        response = get_method(path,client_address)
      elif http_method == 'POST':
        response = post_method(request)

      client_socket.sendall(response.encode())
      client_socket.close()

start_server()
 