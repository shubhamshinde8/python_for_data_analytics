# Generate random number 

import random

jackpot=random.randint(1,100)

# print(jackpot)

guess=int(input('Guess Karo : '))

counter=1

while guess!=jackpot:
 if guess<jackpot:
    print('Galat ! thoda higher ')

 else:
    print('Galat ! Thoda Lower ')

 guess=int(input('Guess Karo : '))
 counter=counter+1
 
else:
  print('Correct Guess ',counter)