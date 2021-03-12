'''
-------------------------------------------------------------------------------
Name:       problem1.py
Purpose:  Determines if Driver was Speeding

Author:    Tan.C

Created:    date in 02/23/2021
------------------------------------------------------------------------------
'''
print("****** Speed Limit ******")

# get speed limit and recorded speed from user
print("Hello")
spd_limit = int(input("Please enter the speed limit: "))
rcd_speed = int(input("Please enter the recorded speed of the car: "))

# compute km/h over speed limit
rcd_minus_spd = rcd_speed - spd_limit

# determine if user is speeding
if rcd_minus_spd >= 1 and rcd_minus_spd <= 20:
  print("You are speeding and your fine is $100.")

elif rcd_minus_spd >= 21 and rcd_minus_spd <= 30:
  print("You are speeding and your fine is $270.")

elif rcd_minus_spd >= 31:
  print("You are speeding and your fine is $570.")

else:
  print("Congratulations, you are within the speed limit!")