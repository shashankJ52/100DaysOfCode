#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("\nWelcome to the tip Calculator!\n")
total_bill = int(input("What was the total Bill ? $"))
tip_amount = int(input("How much tip would you like to give? 10, 12, or 15 ? "))
people = int(input("How many people to split the bill ? "))

per_person_split = round(total_bill * (1+ tip_amount/100) / people, 2)

print(f"\nEach person should pay : ${per_person_split} !!\n")
                 
