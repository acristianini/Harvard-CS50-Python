def main():
    #defining main function

    amount_due = 50
    #setting price of the coke

    while amount_due > 0:
        print("Amount Due: " + str(amount_due))
        amount_paid = int(input("Insert Coin: "))
        #while loop: while you still owe money for the coke, it will keep asking for money

        if amount_paid != 25 and amount_paid != 10 and amount_paid != 5:
            print("Please insert only the approved denominations: 25, 10 or 5 ")
        else:
            amount_due = amount_due - amount_paid
            #making sure the coins are the correct denominations and if they are, updating the money owed for the coke
    else:
        print("Change Owed: " + str(0 - amount_due))
        print("Here is your coke! ")
#once the price of the coke has been payed, correct change is given and the machine says: "here's your coke"

main()
#calling main function
