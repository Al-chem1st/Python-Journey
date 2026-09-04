#by typing input() we can take input from the user.

from cmath import pi


name = input("Enter your name: ")
age = int(input("Enter your age: "))

age = age +2 # its make error be
# its make error because input() always a string value
# for that we just typecast the age variable.

print(f"Hello {name}, I hope you have fun!")
print(f"So, your age is {age}")