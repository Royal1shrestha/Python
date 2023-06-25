# copyfile() = copies contents of file
# copy() = copyfile() + permission mode + destination can be directory
# copy2() = copy() + copies metadata(file's creation & modificaton times)

import shutil,os

source = "F:\\royal\\text.txt"
destination = "F:\\royal\\text2.txt"


shutil.copyfile('F:\\royal\\text.txt','F:\\royal\\copy.txt') #(source,destination)

try:
    if os.path.exists(destination):
        print("A file already exists in destination.")
        
    else:
        os.replace(source,destination)
        print(source + "was moved to destination.")
    # A new file is created and then only data is moved.

except FileNotFoundError:
    print(source + "wasn't found.")
    
# os.remove(path) => delete a file
# os.rmdir(path) => delete an empty directory
# shutil.rmtree(path) => delete a directory containing file