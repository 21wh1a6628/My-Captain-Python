def extension(file):
    file=file.split(".")
    return file[1]

file="abc.py"
print(extension(file))
