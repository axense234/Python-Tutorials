# .find() -finds something in something
# .count() -counts how many items are in something

string = input("Type some shit nigga: ")
print(string.find("h"))
print(string.count("o"))

if string.count("_") != 0:
    print("Not good!")
else:
    print("Good!")