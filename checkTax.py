
salary = float(input("Enter salary: "))

print("NOTE: Your salary between 2 lakh and 20 lakh annually")

if salary < 200000:
    print("No tax applicable")
elif salary <= 300000:
    print("You need to pay", salary * 0.05, "as tax")
elif salary <= 500000:
    print("You need to pay", salary * 0.10, "as tax")
elif salary <= 1000000:
    print("You need to pay", salary * 0.15, "as tax")
elif salary <= 2000000:
    print("You need to pay", salary * 0.20, "as tax")
else:
    print("You need to pay", salary * 0.25, "as tax")