
# lets code celsius to farhnite 


def greet(name):
    return "Hello",{name}


str=input("Enter a Name : ")
print(greet(str))


def add(a,b):
    return a+b


a=int(input('Enter a : '))
b=int(input('Enter B : '))


result=add(a,b)

print(result)


def min_max(numbers):
    return min(numbers), max(numbers)

low, high = min_max([4, 1, 9, 2, 7])
print(low, high)  # 1 9



def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32


celsius=float(input('Enter Celsius : '))

print(celsius_to_fahrenheit(celsius))


def total(*args):
    return sum(args)

print(total(1, 2, 3))        # 6
print(total(10, 20, 30, 40)) # 100


def summarize(*args):
    total = sum(args)          # sum of all numbers
    count = len(args)          # how many numbers
    average = total / count    # average

    return {
        "count": count,
        "sum": total,
        "average": average
    }

print(summarize(10, 20, 30))
{"count": 3, "sum": 60, "average": 20.0}




scores = [85, 92, 78, 90, 88]

print(scores[0])      # 85        → first item
print(scores[-1])     # 88        → last item
print(scores[1:3])    # [92, 78]  → slicing

scores.append(95)     # add to end
scores.remove(78)     # remove a value
scores.sort()         # sort ascending

print(len(scores))    # count of items
print(sum(scores))    # total
print(min(scores))    # lowest
print(max(scores))    # highest


scores.append(88)
print("Maximum Score : ",max(scores),"Minimum Score : ",min(scores))
print("Average Of Scores : ",sum(scores)/len(scores))
print(scores.sort(reverse=True))