# # lets understand python strings 


# # print('python srings ')

# s='shubham shinde'
# s="vaishali susundre"
# s='''shubham shinde'''   # it is used for multiline strings 

# s=str('shubham shinde')

# print(s)

# s="it's raining outside "

# # print(s)




# # Indexing in String 

# # Positive Indexing
# s='Hello world'

# print(s[0])

# # Negetive Indexing 

# print(s[-1])


# # Slicing 

# print(s[0:5])


# str='hey mumbai ! '
# print(str[::-1])


# Editing and Deleting Strings





# name='shubham'
# print(name)

# # python Strings are immutable means we cant edit or modify the strings 

# del name

# # print(name)



# # Operations on Strings 


# # Arithmatic Op

# print('shubham'+' '+'vaishali')


# print('shubham'*5)


# print(
# 'delhi'=='mumbai')







# print('' or 'shubham') # shubham 

# print('' and 'shubham') # blank 

# print('hello' and 'world') # 

# print('hello' or 'world')





# n=int(input('enter n : '))

# fact=1

# for i in range(1,n+1):
#     fact=fact*i



# print(fact)






 # String Functions 

 # Common functions 

str='hello mumbai '
print(len(str))

print(min('helloworld'))

print(str.capitalize())

print(str.title())

print(str.upper())

print(str.lower())

# print(str.swapcase())

print('shubh sHinde'.swapcase())

print('shubhamu shinde'.count('u'))

print('shubham shinde'.endswith('e'))

print('shubham shinde'.startswith('s'))

print('shubham'.find('u'))


name='shubham shinde'
status='single'

print('Hi my name is {} and i am {}'.format(name,status))


print('hi my name is shubham '.split())