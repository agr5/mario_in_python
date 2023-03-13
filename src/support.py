from os import walk


def import_folder(path):
    files = []
    for _,_, file in walk(path):
        files.append(file)
    return files