def main():
    #define main function

    fastspeak = input("Please say something quickly ")
    #assigning user input to variable called fastspeak

    slowspeak = fastspeak.replace(" ", "...")
    #making slowspeak variable replacing blank spaces with ...

    print(slowspeak)
    #print variable slowspeak

main()
#call main function

