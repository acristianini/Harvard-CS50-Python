def convert(text):
    #define function convert with placeholder for text because it will accpet str
    emoji = text.replace(":)", "🙂")
    emoji = emoji.replace(":(", "🙁")
    #assign emoji as variable that is equal to whatever text is put through convert function but with emoticons replaced as emojis
    return emoji
#return emoji variable

def main():
    #define main function
    question = input("Using a happy or sad face, please tell me how you are feeling ")
    #prompt user to input str including emoticon and assign that str to variable called question
    result = convert(question)
    #assign variable result as question put through function convert
    print(result)
    #print result
main()
#call main function

