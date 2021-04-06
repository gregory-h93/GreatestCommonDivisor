print("Welcom to Greatest Common Divisor! I will calculate the greatest common divisor that two numbers of your choosing have in common!")
while True:    #This simulates a Do Loop
    print("Enter in the first number: ")
    num1 = int(input())
    while num1 <= 0:
        print("Invalid input! Please enter a number greater than 0: ")
        num1 = int(input())
    print("Enter in the second number: ")
    num2 = int(input())
    while num2 <= 0:
        print("Invalid input! Please enter a number greater than 0: ")
        num2 = int(input())
    while num1 != num2:
        if num1 > num2:
            num1 = num1 - num2
        else:
            num2 = num2 - num1
    print("The greatest common divisor of your numbers is " + str(num2))
    print("Would you like to run the program again? (Y/N)")
    again = input()
    while again != "Y" and again != "y" and again != "N" and again != "n":
        print("Please enter in (Y/N). Would you like to run the program again? (Y/N)")
        again = input()
    if not(again == "Y" or again == "y"): break   #Exit loop
print("You have chosen to end the program. Goodbye!")
