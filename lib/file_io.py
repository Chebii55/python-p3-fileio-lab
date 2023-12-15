def write_file(file_name, file_content):
    full_name = str(file_name)+ '.txt'
    with open(full_name, mode='w', encoding='utf-8') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    full_name=str(file_name)+'.txt'
    with open(full_name, mode='a', encoding='utf-8') as file:
         file.write(append_content)

def read_file(file_name):
    full_name = str(file_name) + '.txt'
    with open(full_name, encoding='utf-8') as text_file:
        return text_file.read()
    