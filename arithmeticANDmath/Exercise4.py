#Calculate the hypotenuse

import math

a=round(float(input("Enter a: ")),2)
b=round(float(input("Enter b: ")),2)

c=math.sqrt(pow(a,2)+pow(b,2))

print(f"The hypotenuse = {round(c,2)}cm^2")