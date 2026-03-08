
#understand the if else statement in python 


userEmail=input('Enter email ')
Userpassword=input('Enter Password ')


if userEmail=='shubhamshinde8746@gmail.com' and Userpassword=='Shubham@123':
    print('Access Granted !')
elif userEmail=='shubhamshinde8746@gmail.com' and Userpassword!='Shubham@123':
    print('Wrong Password ')
    print('Please Enter again ')

    Userpassword=input('Enter Correct Password : ')

    if Userpassword=='Shubham@123':
        print('Welcome Finally ! ')
    else:
        print('Beta Tumse na Ho payega !! ')
else:
    print('Please Enter correct Email and Password !')


a=int(input('Enter 1st Number : '))
b=int(input('Enter 2nd Number : '))


op=input('Enter Operator : ')


if op=='+':
    print(a+b)
elif op=='-':
    print(a-b)
elif op=='*':
    print(a*b)
else:
    print(a/b)



Moduls in python 

import math
# print(math.sqrt(12))

import keyword
# print(keyword.kwlist)

import datetime
print(datetime.datetime.now())


import random
print(random.random)

help('modules')