import math
print("Welcome to the Right Triangle Solver App")

# Get user inputs
firstleg = float(input("\nWhat is the first leg of the triangle: "))
secondleg = float(input("What is the second leg of the triangle: "))

# Calculation
hypotenuse = math.sqrt(firstleg**2 + secondleg**2)
hypotenuse_round = round(hypotenuse, 3)
area = round(firstleg*secondleg)/2
area_round = round(area, 3)

# Output
print("\nFor a triangle with legs of " + str(firstleg) + " and " +
      str(secondleg) + " the hypotenuse is " + str(hypotenuse_round))
print("For a triangle with legs of " + str(firstleg) + " and " +
      str(secondleg) + " the area is " + str(area_round))
