import os


def createTxtFiles(file_path: str, file_name: str):
    file_name_initial = file_name.split(".")[0]
    final_directory = os.path.join(file_path, file_name_initial+".txt")
    file = open(final_directory, 'w')
    file.write('Created on:')
    file.close()
    print(f"Created file named:{final_directory}")
    # deleteFromDirectory(os.path.join(file_path, file_name))
