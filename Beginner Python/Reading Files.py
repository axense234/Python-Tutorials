
# open("employees", "r")-Read Mode
# open("employees", "w")-Write Mode
# open("employees", "a")-Add Mode
# open("employees", "r+")-Read and Write Mode

employee_file = open("employees", "r")

# print(employee_file.readable())-To check if a file is readable
# print(employee_file.read())-Reads the whole file
print(employee_file.readline())
print(employee_file.readline())
print(employee_file.readlines()[2])
employee_file.close()
