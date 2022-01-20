import os


def filename_from_path(path:str):
    return os.path.split(path)[-1]

