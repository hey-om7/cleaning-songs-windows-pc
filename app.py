from pickFile import pickFile
from getFileNames import get_file_names
from deletingFiles import deleteFromDirectory
from createTextFiles import createTxtFiles
import os


directory_path = pickFile()

file_names = get_file_names(directory_path)


for file_full_name in file_names:
    createTxtFiles(os.path.dirname(file_full_name),
                   os.path.basename(file_full_name))
    deleteFromDirectory(file_full_name)
