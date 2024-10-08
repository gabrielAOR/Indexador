import os
import glob

def find_string(start_str, string, end_str="-----"):
  try:
    start_index = string.find(start_str)
    end_index = string.find(end_str, start_index + len(start_str))

    result = string[start_index + len(start_str):end_index]

    return result.strip()

  except ValueError:
    return "Valor passado incorreto"
  
def read_file(path):
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
  text_to_find = find_string('\"\r\nContent-Type:',request,end_str='\n')

  filename = find_string("filename=\"", request, end_str='\"')

  file_content = find_string(text_to_find, request)
  store_file(folder_name, file_content, filename)  


def find_first_html_file(folder_path):
  html_files = glob.glob(os.path.join(folder_path, '*.html'))
  
  if html_files:
    return os.path.basename(html_files[0])
  else:
    return None
