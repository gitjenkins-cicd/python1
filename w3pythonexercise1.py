import sys
print(sys.version_info)

# date and time

import datetime
now=datetime.datetime.now()
print(now.strftime("%Y-%m-%d %H:%M:%S"))

# calculating area
from math import pi
r=float(input("Input the redius of the circle: "))
print("The are of the circle  with redius  " + str(r) + " is: " + (str(pi*r**2)))

# reversing names
fname=input("Please Enter your first Name: ")
lname=input("Please Enter your last Name: ")
print("your lastname is " + lname + " Your first Name is " + fname)

# Generate list and tuple based on user inputs
values=input("Enter few Numbers: ")
list=values.split(",")
print("List is :", list)
tuple=tuple(list)
print("Tuple is :",tuple)

# Displaying first and last color
color_list = ["Red","Green","White" ,"Black"]
print("%s%s" % (color_list[0], color_list[-1]))

# input an integer and compute n+nn+nnn
val=int(input("Enter a value: "))
print("%s" % val)
print("%s%s" % (val,val))
print("%s%s%s" % (val,val,val))

