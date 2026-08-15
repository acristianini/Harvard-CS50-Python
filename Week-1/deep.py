def main():
    #defining main function

    question = input("What is the answer to the Great question of life the universe and everything? ").strip().casefold()
    #assigning variable question to the user's (not case sensitive) input when prompted the question

    compare(question)
    #calling compare function and funneling user input to question through

def compare(x):
    #defining compare function and preparing it to accept a string

    if x == "42" or x == "forty two" or x == "forty-two":
        print("Yes ")
        #conditional: if the answer to question is 42 in any form, then deep.py will print yes
    else:
        print("No ")
        #in every other case, deep.py will print no.

main()
#calling main function

