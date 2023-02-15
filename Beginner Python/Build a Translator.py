def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter.lower() in "aeiou":
            if letter.isupper():
                translation = translation + "G"
            else:
                translation = translation + "g"

        else:
            translation = translation + letter
    return translation

print(translate(input("Enter a phrase: ")))

# Damn this is getting complicated but this is a good example of combining all the stuff i learned
