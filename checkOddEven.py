
# check odd or even

# numbers=[12,4,3,5,7,34,21,56]

# for n in numbers :
#     if n%2==0 :
#         print('number is even ')
#     else:
#         print('number is odd ')




# The Password Protector


# secret = "python123"
# guess = ""

# while guess != secret:
#     guess = input("Enter the secret password: ")
#     if guess == secret:
#         print("Access Granted!")
#     else:
#         print("Wrong! Try again.")


# Check Number is 3 digit or not 

num=int(input('Enter a number '))

if num>99 and num<1000:
    print('Number is 3 digit !')

elif num>9 and num<100 :
    print('Number is 2 digit ')

else:
    print('number is not in correct range ! ')