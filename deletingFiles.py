import os


def deleteFromDirectory(file_path: str):
    if (os.path.basename(file_path).split(".")[1] != "txt"):
        print(f"Deleting file:{file_path}")
        os.remove(file_path)
