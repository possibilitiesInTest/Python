import os
print(os.getcwd())

os.chdir("C:/Users/goura/Desktop")
print(os.getcwd())
print(os.listdir())


if "myfolder" not in os.listdir():
    os.mkdir("myfolder")

print(os.listdir())

for dirpath, dirnames, filenames in os.walk("C:/Users/goura/Desktop/myfolder"):
    print(dirpath)
    print(dirnames)
    print(filenames)

print(os.path.join(os.envrion.get("HOME"), "myfile.text"))

# get basename, file at the directory location given
os.path.basename("/bin/tools/myfile.txt")

# get directory name only
print(os.path.split("/bin/tools/hello/balbala/myfile.txt"))

# Will give directory name and basename in a tuple
os.path.split("/bin/tools/hello/balballa/myfile.txt")

# check if path exists
print(os.path.exists("/bin/tools/hello/balbala/myfle.txt"))

# used to check if file exists in the specified path
print(os.path.isdir("/dir/tools/hello/balbala/myfile.txt"))

# splits filename from file format
print(os.path.splitext("/bin/tools/hello/balbala/myfile.txt"))


import sys

print(sys.argv[1:])


