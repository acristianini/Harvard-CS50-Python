def main():
    #defining main function

    which_fruit = input("Item: ").casefold().strip()
#defining variable which_fruit as the user input when prompted for a fruit
#the user input is converted to lowercase and has all free space stripped so that it conforms with dictionary key syntax

    calorie_count(which_fruit)
    #calling calorie_count function and passing user input through it

def calorie_count(which_fruit):
    #defining calorie_count function and priming it to pass a str through it 

    fruits = {"apple": "130 ", "avocado": "50 ", "banana": "110 ", "cantaloupe": "50 ", "grapefruit": "60 ", "grapes": "90 ", "honeydew melon": "50 ",
           "kiwifruit": "90 ", "lemon": "15 ", "lime": "20 ", "nectarine": "60 ", "orange": "80 ", "peach": "60 ", "pear": "100 ", "pineapple": "50 ",
             "plums": "70 ", "strawberries": "50 ", "sweet cherries": "100 ", "tangerine": "50 ", "watermelon": "80 " }
    #creating dictionary called fruits, assigning each fruit a calorie value

    if which_fruit in fruits:
        print(f"""
Calories: {fruits[which_fruit]}
""")
    else:
        print("")
#printing resulting fruits calories by calling the dictionary and using the user input as the key to search for the value within the dictionary
#if user input isn't in the dicitonary, print blank space

main()
#calling main function