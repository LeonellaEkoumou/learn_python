#bmi calculator
print('bmi calculator')
height=float(input("enter your height in m:"))
weight=float(input("enter your weight in kg:"))
bmi=weight/(height**2)
print("your bmi is:",bmi)
print("reminder: bmi under 18.5 is underweight, 18.5 to 24.9 is normal weight, 25 to 29.9 is overweight, and 30 or above is obese")