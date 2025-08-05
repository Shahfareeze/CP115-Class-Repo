# Import Math module
import math
radius_of_circle = float(input("Enter radius: "))

# calculate circle area
circle_area = ( (2 ** radius_of_circle) * math.pi)
#calculate circumference of the circle
circumference_of_circle = 2*(math.pi * (radius_of_circle))

#Output
print()
print("Circle area : " + str(circle_area))
print("Circumference of circle : " + str(circumference_of_circle))

