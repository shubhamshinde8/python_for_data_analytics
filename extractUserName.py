# extract the username from mail

mail='shubhamshinde8746@gmail.com'

name=''

for i in mail:
    if i=='@':
        break
    name=name+i


print(name)