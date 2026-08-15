def main():
    #define main function

    camel = input("Please input the name of your variable in camel case ")
    #assign variable camel as the input str when user is prompted for the name of their variable in camel case

    convert(camel)
    #call convert function, pass through user input

    print()
    #blank print to move to new line
    
def convert(camel):
    #define convert function, design to take string

    camel_case = camel
    #assing variable camel_case as the string taken by convert function

    for letter in camel_case:
        if letter.isupper():
            print("_" + letter.lower(), end = "")
        else:
            print(letter, end = "")
#for loop, check every letter in input str, if the letter is uppercase: print _ before it and the lowercase version of the letter, if it isn't upper case just print the letter, no new line at the end of the print.


main()
#call main function