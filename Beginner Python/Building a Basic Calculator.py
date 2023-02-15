

num_1 = input("Enter a number: ")
num_2 = input("Enter another number:8 ")
result = num_1 + num_2
print(result)
# Without anything,Python will always think of the inputs as string
num_1 = input("Enter a number: ")
num_2 = input("Enter another number: ")
result = int(num_1) + int(num_2)
print(result)
# int transforms strings into WHOLE numbers
# float transforms strings into DECIMAL numbers and WHOLE numbers