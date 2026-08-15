def main():
    #defining main function

    question = input("Hello ").strip().casefold()
    #assigning question variable prompting greeting as user input, disregarding whitespace arount str and making it case insensitive

    compare(question)
    #calling compare function and inputing question value

def compare(x):
    #defining compare function, and priming it to accept strings
    if x == "hello":
        print("$0 ")
    #conditional: if greeting is hello, the output is $0

    elif x == "hello, newman":
        print("$0 ")
    #conditional: if the greeting is hello newman, the output is $0

    elif x[0] == "h":
        print("$20 ")
    #conditional: if the first letter of the greeting is 'h', then the output is $20

    else:
        print("$100 ")
    #conditonal: in all other cases, the output is $100

main()
#calling main function

