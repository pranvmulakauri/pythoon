print("Task 1")
age = int(input("Enter your age (integer value only): "))
if age<18:
    print("Sorry you are not eligible for a loan.")
else:
    salary = int(input("Enter your annual income (integer value only): "))
    if salary >= 1500:
        print("You are eligible for a loan.")
    else:
        print("Sorry you are not eligible for a loan.")
print(" ")

print("Task 2")
age_task_2 = int(input("Enter your age(integer value only): "))
if age_task_2 < 21:
    print("You cannot enroll on the course.")
else:
    qualification = input("Are you qualification(Y/N): ")
    if qualification == "Y":
        print("You can enroll on the course.")
    else:
        print("You cannot enroll on the course.")
print(" ")

print("Task 3")
a = int(input("Enter the first value(a): "))
b = int(input("Enter the seconde value(b): "))
if a>=b:
    c = a/b
    c = int(c)
    print(f"The number of times the second number can be divided into the first number is {c}.")
else:
    print("The second number is larger than the first number therefor it is not possible to divide.")