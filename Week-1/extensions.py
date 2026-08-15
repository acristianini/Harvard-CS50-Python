def main():
    #defining main function

    file_name = input("What is the name of your file? ").strip().casefold()
    #assigning variable file_name to the user input after being prompted for the name of the file, ignoring whitespace and case insensitive

    media_type(file_name)
    #calling media_type function and running file_name variable through it

def media_type(x):
    #defining media_type function and priming it to take str

    match x:
        case _ if ".gif" in x:
            print("image/gif ")
        case _ if ".jpg" in x:
            print("image/jpeg ")
        case _ if ".jpeg" in x:
            print("image/jpeg ")
        case _ if ".png" in x:
            print("image/png ")
        case _ if ".pdf" in x:
            print("application/pdf ")
        case _ if ".txt" in x:
            print("text/plain ")
        case _ if ".zip" in x:
            print("application/zip ")
        case _:
            print("application/octet-stream ")
    #searching through string x (the user input) for any of the above file extensions and printing out the corresponding media type if present
    #else printing application/octet-stream as a catch all error message

main()
#calling main function

        
        
    
    




    





    

