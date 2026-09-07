# weight converstion with python 

weight = float(input("Enter your weight: "))
unit = input ("kilograms or Pound? (k or p): ")

if unit == "k":
    weight = weight * 2.205
    unit = "Lps"
elif unit == "p":
    weight = weight / 2.205
    unit = "Kgs"
else :
    print(f"{unit} is not valid")

print (f"Your weight is :{round(weight, 2)}")