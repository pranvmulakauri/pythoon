# Check leap year
print("Task 1")
y = int(input("Enter the year (+ve integer): "))
if y > 0:
    if y % 4 == 0:
        if y % 100 == 0:
            if y % 400 == 0:
                print(f"{y} is a leap year.")
            else:
                print(f"{y} is divisible by 100 but not by 400, so it is not a leap year.")
        else:
            print(f"{y} is a leap year.")
    else:
        print(f"{y} is not a leap year.")
else:
    print("Invalid year entered.")
print("\n")
# Check triangle angles
print("Task 2")
a = int(input("Enter the bottem left angle of a triangle: "))
b = int(input("Enter the top angle of a triangle: "))
c = int(input("Enter the bottem right angle of a triangle: "))
sum_of_angles = a+b+c
if sum_of_angles == 180:
    if a == 90:
        print("It is a left Right angle triangle.")
    elif b == 90:
        print("It is a right Right angle triangle.")
    elif c == 90:
        print("It is a top Right angle triangle.")
    else:
        print("The provided angles are not of a right angle triangle.")
else:
    print("The angles provided ar not that of a triangle")
print("\n")
# Pattern print
print("Task 3")
x = int(input("Enter the number of lines or the maximum number of row you want in the triangle made of '*':"))
for i in range(1, x-1):
    print(" " * (x - i) + "*" * (2 * i - 1))
print("\n")
