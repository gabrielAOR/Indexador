import os

def find_string(start_str, string, end_str="-----"):
  try:
    start_index = string.find(start_str)
    end_index = string.find(end_str, start_index + len(start_str))

    result = string[start_index + len(start_str):end_index]

    return result.strip()

  except ValueError:
    return "Valor passado incorreto"
  
def read_file(path):
  """Read and return the content of a file."""
  if os.path.exists(path) and os.path.isfile(path):
    with open(path, 'r') as file:
      content = file.read()
    return content
  else:
    return None
  
def store_file(folder, content, filename):
  if not os.path.exists(folder):
    os.makedirs(folder)

  file_path = os.path.join(folder, filename)

  with open(file_path, 'w') as file:
    file.write(content)

def handle_post(request):
  folder_name = find_string("siteName\"", request)
  text_to_find = {'text/html':"index.html", 'text/css':"style.css", 'application/x-javascript':"script.js"}

  for key, value in text_to_find.items():
    file_content = find_string(key, request)
    store_file(folder_name, file_content, value)
  
