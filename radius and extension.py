r=float(input("enter the radius: "))
area=3.14*r**2
print("Area of the circle with radius",r,"is:",area)

def extension(file):
    file=file.split(".")
    return file[1]

file="abc.py"
print("File extension is :",extension(file))
