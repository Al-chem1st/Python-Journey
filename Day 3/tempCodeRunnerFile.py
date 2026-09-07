# weight converstion with python 

weight = float(input(Enter your weight: ))
unit = input ("kilograms or Pound? (K or P): ")

if unit == "K":
    weight = weight * 2.205
elif unit == "P":
    weight = weight / 2.205
else :
    print(f"{unit} is not valid")

print (f"Your weight is :{weight}")