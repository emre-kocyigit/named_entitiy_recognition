import os
from bs4 import BeautifulSoup


def read_file(file_path):
    file = open(file_path, 'r')
    return file.read()


def extract_text(content):
    soup = BeautifulSoup(content, "html.parser")
    return soup.get_text(strip=True)


def create_text_dict(path):
    os.chdir(path)
    dict_list = list()
    for file in os.listdir():
        if file.endswith(".html"):
            file_path = f"{path}/{file}"
            content = read_file(file_path)
            temp_text = extract_text(content)
            dict_list.append({"name":file, "text":temp_text})
        else:
            pass
    return dict_list
