
# if condition == True:
#     do this

age = input("Input your age: ")
if int(age) > 16:
    print("Hey,you are older than 16!")
else:
    print("You are younger than 16!")

height = input("Please enter your height: ")
if int(height) < 1:
    print("You cannot ride,you are under 1m!")
elif int(height) > 2:
    print("You cannot ride,you are over 2m!")
else:
    print("You can ride!")
