import os


def filename_from_path(path:str):
    return os.path.split(path)[-1]


def load_txt(filename: str):
    content = 'ERROR: Only .txt files allowed'

    if filename.endswith('.txt'):
        fp = os.path.join(os.path.dirname(__file__), filename)

        with open(fp, 'r', encoding='utf-8') as f:
            content = f.read()

    return content
