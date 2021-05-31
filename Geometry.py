# averagespeed.py
# a.peer
# March 5, 2020
# To calculate the average speed of a car

#import-math
import math
PI=math.pi

#Title
print(" --------------------------------------------")
print(" Surface Area and Volume Of Cylinder Calculator")
print(" --------------------------------------------")

#User-Input
height = float( input(" Enter Height of Your Cylinder: "))
radius = float( input(" Enter Radius of Your Cylinder: "))

#Calculations
surfaceArea= (((2*(PI))*(height*radius))+((2*(PI))*((radius)**2)))
volume=((PI)*((radius**2)*height))
volume=round(volume, ndigits=1)
surfaceArea=round(surfaceArea, ndigits=1)

#output
print("\n","The Surface Area of Your Cylinder Is: ",surfaceArea)
print(" The Volume of Your Cylinder Is",volume)
