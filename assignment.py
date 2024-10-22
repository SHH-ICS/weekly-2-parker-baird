import math

print("What is the Diameter?")
D = float(input())
radius = D / 2
A = math.pi * radius ** 2
C = 2 * math.pi * radius

print("The Area is...")
print(A)
print("The Circumference is...")
print(C)