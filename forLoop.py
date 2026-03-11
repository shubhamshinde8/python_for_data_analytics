# for loop in python 


# for i in range(1,10):
#     print(i*3)




# str='Delhi'

# for i in (str):
#     if i=='l':
#         print(i)



# The current population of a town is 10000. The population of the town is incresing at 
# the rate of 10% per year. You have to write a program to find out the population at the
# end of each of the last 10 years .



# solution ---> 

curr_population=10000

for i in range (10,0,-1):
    print(i,curr_population)
    curr_population=curr_population-0.1*curr_population

    

