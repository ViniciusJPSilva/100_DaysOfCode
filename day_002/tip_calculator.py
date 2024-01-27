#If the bill was $150.00, split between 5 people, with 12% tip. 
#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60
#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

PERCENTAGES = [10, 12, 15]

total_bill = 0
percentage = 0
number_of_people = 0

print("\nWelcome to the tip calculator!")

try: 
    while total_bill <= 0:
        total_bill = float(input("\nWhat was the total bill?\nR$ "))
        if total_bill <= 0:
            print("\nWARNING: Total bill must be greater than 0!")

    while percentage not in PERCENTAGES:
        percentage = int(input("\nWhat percentage tip would you like to give? 10, 12 or 15?\n"))
        if percentage not in PERCENTAGES:
            print("\nWARNING: Invalid percentage!")

    while number_of_people <= 0:
        number_of_people = int(input("\nHow many people to split the bill?\n"))
        if number_of_people <= 0:
            print("\nWARNING: Number os people must be greater than 0!")

    splited_total = (total_bill / number_of_people) * (1 + percentage / 100)
    print("\nEach person should pay: R$ {:.2f}\n".format(splited_total))
except ValueError:
    print("\nError: An invalid value was entered! The program will be terminated!\n")
except KeyboardInterrupt:
    print("\nThe program has been terminated!\n")


