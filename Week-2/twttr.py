def main():
#defining main function

    original_str = input("Input: ")
    #assinging variable to user input

    remove_vowels(original_str)
    #calling function that removes vowels from original str (the users input)
    print()
    #blank print to force new line for asthetics

def remove_vowels(x):
    #defining function that removes vowels, designed to take a str

    vowels = ["A", "a", "E", "e", "I", "i", "O", "o", "U", "u"]
    #defining list of vowels in both upper and lowercase
    
    for char in x:
        if char in vowels:
            print("", end = "")
        else:
            print(char, end = "")
#for loop that checks every character in the user input str against the list of vowels and either prints the character if it isnt in the list or doesn't print anything if it is a vowel


main()
#calling main function