
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
else:
    print("You are neither male nor tall")


if is_male and is_tall:
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not is_male and is_tall:
    print("You are not a male but tall")
    print("You are a short male")
else:
    print("You are not a male and not tall")

# Very complex and fun
