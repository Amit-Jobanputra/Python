# def add(*num):
#     a=0
#     for i in num:
#         a=a+i
#     print(a)
# add(1,2,3)

# mul= int(input("Enter The Number you want The Table:- "))
# for i in range(1,11):
#     print(f"{mul}x{i}={mul*i}")

# states=['gujarat','maharastra',"karnatka"]
# capitals=['Gandhinager','mumbai','bengaluru']
# dict1={}
# for i in range(len(states)):
#     dict1[states[i]]=capitals[i]
# print(dict1)

# from numpy import *
# arr=[30,40,20,10,40]
# total=0
# length = len(arr)
# for i in range(length):
#     total =total+ arr[i]
# avg=total/length
# print(total)
# print(avg) 

import re

text = "Hello@world!!This-is#Python$123 1"

# Split where one or more non-alphanumeric characters are found
parts = re.split(r'\W+', text)
parts1 = re.findall(r'\b\d\b', text)
parts2 = re.findall(r'\b\w{5,}\b', text)

print(parts)
print(parts1)
print(parts2)
