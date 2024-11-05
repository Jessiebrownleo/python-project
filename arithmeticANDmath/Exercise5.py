#Calculate the distance between two points

import math

x1=float(input("Enter X1: "))
x2=float(input("Enter X2: "))
y1=float(input("Enter Y1: "))
y2=float(input("Enter Y2: "))

distance = math.sqrt((math.pow(x2-x1,2))+(math.pow(y2-y1,2)))

print(f"The distance is {distance}")