#Input is taken for height in  meter and weight in kg and BMI is calculated. It is also rounded off to a nearest whole number. 
#Later based on BMI definitions a message is displayed to user about their BMI and corresponding health implications
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))


bmi=round(weight/(height ** 2))


if bmi < 18.5:
  print(f"Your BMI is {bmi}, you are underweight.")
elif bmi < 25:
  print(f"Your BMI is {bmi}, you have a normal weight.")
elif bmi < 30:
  print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi < 35:
  print(f"Your BMI is {bmi}, you are obese.")
else:
  print(f"Your BMI is {bmi}, you are critically obese.")


#earlier I tried using if bmi >18.5 & bmi <25, but it was giving me Type error: assuming they both are not same datatype
