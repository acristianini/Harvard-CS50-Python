def main():
    #defining main function

    dollars = dollars_to_float(input("How much was the meal? "))
    #assigning variable dollars to the user inputing the cost of the meal and calling dollars to float function, which converts the str input to a float

    percent = percent_to_float(input("What percentage would you like to tip? "))
    #assinging variable percent to the user inputing the percentage they would like to tip and calling the percent to float function, which converts the str input to a float

    tip = dollars * percent
    #assigning tip variable as the product of the dollars and percent variables

    print(f"Leave ${tip:.2f}")
    #Printing the text, inserting the 'tip' variable rounded to 2 decimal places


def dollars_to_float(d):
    #defining dollars to float function

    dollars = d.replace("$", " ")
    #assigning dollars variable as the str input to the function replacing all $ signs with a space

    dollars_float = float(dollars)
    #assigning dollars_float variable as the value of the dollars variable converted to a float

    return dollars_float
#returning dollars_float value so it can be used in main function


def percent_to_float(p):
    # defining percent_to_float function

    percent = p.replace("%", " ")
    #assigning percent variable as the str input to the function replacing all % signs with a space

    percent_float = float(percent)
    #assigning percent_float variable as the value of the percent variable converted to a float

    percent_multiplyer_float = percent_float / 100
    #assigning percent_multiplyer_float variable as the percent_float value / 100 so that it can be used as a decimal multiplyer

    return percent_multiplyer_float
#returning percent_multiplyer_float value so that can be used in the main function


main()
#calling main function
