with open("sample.txt", "w") as f:
    f.write("My name is Arsen\n")
    f.write("I am KBTU student which is specialized in Informational Systems\n")
    f.write("I love c++\n")

with open("sample.txt", "a") as f:
    f.write("c++ top\n")
    f.write("KBTU one love\n")

with open("sample.txt", "r") as f:
    print(f.read())