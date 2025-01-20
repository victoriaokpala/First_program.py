import math  # Ive imported the math library to be able to calculate for pi

print("Welcome to the Circle Calculator program!") # This is to greet the user 

radius = float(input("Please enter the radius of the circle: ")) # Prompt the user to enter the radius

diameter = 2 * radius # formula to calculate the diameter

circumference = 2 * math.pi * radius  # formula to calculate the circumference

area = math.pi * (radius ** 2) # Now we calculate the area
# Print the calculated results to the user
print(f"The diameter of the circle is: {diameter}")
print(f"The circumference of the circle is: {circumference}")
print(f"The area of the circle is: {area}")
print(f"Thank you for using the program")
