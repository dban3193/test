#This is my Day-2 project using basic python concepts. Create a tip calculator using total bill, percentage of tip and number of persons to split the bill into.

print("Welcome to the tip calculator")
total=float(input("What was the total bill? $"))
tip=int(input("what percentage tip would you like to give? 10,12, or 15? "))
persons=int(input("how many persons to split the bill? "))

total_after_tip=total+total*tip*0.01
#per_person=round(total_after_tip/persons,2)
#the above wont give accurate results if we have a clean division with no lingering.To fix that, we use format function
per_person="{:.2f}.format(total_after_tip/persons)

print(f"Each person should pay: ${per_person}")
