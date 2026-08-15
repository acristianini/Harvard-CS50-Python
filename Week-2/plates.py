def main():
    #defining main function 

    plate = input("Plate: ")
    #assigning plate variable as the user input when prompted for the licence plate

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")
#checking if the inputted licence plate is valid by calling the is_valid function and running the palte variable through it 
#if plate is valid print valid, if plate is not valid, print invalid

def is_valid(s):
#defining is_valid function and prepping it to take a str

    plate = s 
    #defining str passed through function as "plate"

    if 2<= len(plate) <= 6:
        pass
    else:
        return False
#ensuring the character length of plate is between 2 and 6, if it isnt, the function returns invalid

    if plate[0:2].isalpha():
        pass
    else:
        return False
#making sure the first two characters of the plate are letters rather than numbers, if not, the function returns that the plate is invalid

    seen_digit = False
    #defining seen_digit as false, this is a flag used to indicate whether an number has been seen in the licence plate yet while going through character by character

    for index, char in enumerate(plate):
#enumerate breaks up the str passed through it character by character and assigns each one a numerical position in the str
#here i am creating a for loop, and passing the plate str through the enumerate function
        if char.isalpha() and seen_digit == True:
            return False
        else:
            pass
        #if the character in the licence plate is a letter but a number has already been used, then the plate is invalid

        if char.isdigit() and seen_digit == False:
            seen_digit = True
            if char == "0":
                return False
            else:
                pass
#if the character in the plate is a number, and we havent seen a number yet, seen_digit is true because we have seen a number
#but if we see a digit for the first time that is 0, then the plate is invalid

        if not char.isalnum():
            return False
        else:
            pass
        #if the characters in the licence plate are anything but letters or numbers, then the plate is invalid. this prevents punctuation

        pass
    return True
#if the licence plate passes all these conditions, then the function returns true and the licence plate is valid





main()
#calling main function
