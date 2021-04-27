# # import calendar
# # year=int(input("Please enter year: "))
# # month=int(input("Please enter month: "))
# # print(calendar.month(year, month))
# #
#
# from datetime import date
# ldate=date(2021,4,22)
# rdate=date(2020,3,22)
# deldate=ldate - rdate
# print(deldate)
#
# # Write a Python program to get the difference between a given number
# # and 17, if the number is greater than 17 return double the absolute difference.
# def difference(n):
#     if n < 17:
#         return 17 -n
#     elif n==100:
#         return (n - 17) * 2
#     else:
#         return (print("enter valid input"))
# print(difference(100))
# test whether a number is within 100 of 1000 or 2000
def nearthousand(n):
    return ((abs(1000 -n) <= 100) or (abs(2000 -n) <= 100))
print(nearthousand(400))

# calculate the sum of three given numbers, if the values are equal then return thrice of their sum

def sumthrice(x,y,z):
    sum=x+y+z
    if x==y==z:
        sum=sum*3
    return sum
print(sumthrice(4,4,4))

# get a new string from a given string where "Is" has been added to the front.
# If the given string already begins with "Is" then return the string unchanged.

def isfunc(str):
    print(len(str))
    if len(str) >=5 and str[:2] == "IS":
        return str
    return "IS" + str

print(isfunc('ahmedss'))

# Write a Python program to get a string which is n (non-negative integer) copies of a given string.
def larger_num(str,n):
    result=""
    for i in range(n):
        result=result + " " + str
    return result

print(larger_num('shakeer',5))
# Write a Python program to count the number  in a given list.
def list_count(nums):
    count=0
    for num in nums:
        if num == 4:
            count = count + 1
    return count
print(list_count([4,5,6,4,1,2,3,4]))
# Write a Python program to get the n (non-negative integer) copies of the first 2 characters
# of a given string. Return the n copies of the whole string if the length is less than 2.
def ncopies(str,n):
    flen=2
    if flen > len(str):
     flen=len(str)
    substr=str[:flen]
    result=""
    for i in range(n):
        result=result+ substr
    return result
print(ncopies('Shakeer',5))

# Write a Python program to test whether a passed letter is a vowel or not.

def isvowel(char):
    allvowels="aeiou"
    return char in allvowels

print(isvowel('z'))

# create a histogram from a given list of integers
def histogram(items):
    for n in items:
        output=''
        times=n
        while (times >0 ):
            output=output + '*'
            times=times -1
        print(output)
print(histogram([3,4,5]))


























