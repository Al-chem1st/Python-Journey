# how to calculate the circumference of a Circle ,2πr
import math 

radius = float(input("Enter the radius of the circle: "))
area = 2*math.pi*radius

print(f"The circumference is :{round(area, 2)}cm")     #round() means its only take 2 decimal points