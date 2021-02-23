'''
-------------------------------------------------------------------------------
Name:       problem2.py
Purpose:  Determines Whether a Figure is a Triangle

Author:    Tan.C

Created:    date in 02/23/2021
------------------------------------------------------------------------------
'''
print("****** Triangles ******")

# get side lengths from user
print("Hello")
side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))

# determine if figure is triangle
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
  print("The figure is a triangle.")

else:
  print("The figure is NOT a triangle.")