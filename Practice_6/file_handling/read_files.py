with open("sample.txt", "r") as f:
    content1 = f.read()
    print(content1)
    content2 = f.readline()
    print(content2)
    content3 = f.readlines()
    print(content3)