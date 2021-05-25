# project.py - Accepts two name as input and returns it as a string

def names():
    while True:
        first_name = input("Enter your name:")
        second_name = input("Enter the other person's name : ")
        counter1 = 0
        counter2 = 0

        first_name = first_name.upper()
        second_name = second_name.upper()

        first_name_list = first_name.split()   # used to remove white spaces
        second_name_list = second_name.split()
        first_name_final_list = []
        second_name_final_list = []
        for word in first_name_list:
            for letter in word:
                counter1 += 1                             
                if letter.isalpha():                  # only letters are added
                    first_name_final_list.append(letter)
                    
        for word in second_name_list:                   # if the counter gets incremented and the letter dosen't it means that it is not alphabetical
            for letter in word:
                counter2 += 1
                if letter.isalpha():
                    if letter.isalpha():
                        second_name_final_list.append(letter)
                   
        if (len(first_name_final_list) == counter1 and len(second_name_final_list) == counter2 ):
            break
        else:
            print("Only letters and white spaces are allowed")
            
        

    return first_name_final_list , second_name_final_list


def commom_alphabets(first_name , second_name):
    common = []
    for letter in first_name:
        if (letter in second_name and not letter in common ):
            common.append(letter)
            
    return common


