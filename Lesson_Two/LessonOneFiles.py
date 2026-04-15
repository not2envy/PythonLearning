#with = automatic cleanup (like 'using' in C#)
with open("data.txt", "r") as file:
    content = file.read()
    print(content)