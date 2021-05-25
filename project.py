# project.py - Accepts two name as input and returns it as a string

def names():
    while True:
        first_name = input("Enter your name:")
        second_name = input("Enter the other person's name : ")

        if (first_name.isalpha() and second_name.isalpha()):
            break
        else:
            print(" -- Only letters are allowed in name --")

    first_name = first_name.upper()
    second_name = second_name.upper()

    return first_name , second_name

def commom_alphabets(first_name , second_name):
    common = []
    for letter in first_name:
        if (letter in second_name and not letter in common ):
            common.append(letter)
            
    return common

names()
