def main():
    #defining main function

    c = 300000000
    #assigning varibale C as speed of light in m/s

    m = int(input("Please enter the mass in kg "))
    #assigning m as the integer input from user in kg

    e = m * c**2
    #defining e as energy = mass*speed of light ^2

    print("Energy is equal to ", + e, "joules")
    #printing value of e concatenated with str explaining the value.

main()
#calling main function

