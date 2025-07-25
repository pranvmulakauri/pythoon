# Maximum of three given numbers
def maximum(a,b,c):
    if a>b and a>c:
        return a
    elif b>a and b>c:
        return b
    else:
        return c

def maximum_n(n):
    num_max = max(n)
    return num_max

# Printable for max of three
a = int(input("Enter a value for a: "))
b = int(input("Enter a value for b: "))
c = int(input("Enter a value for c: "))
print(f"The maximum among a,b and c is: {maximum(a,b,c)}")

# Printable for max of n number of given inputs taken as list
num = list(map(int, input("Enter numbers separated by space: \n").split())) #Using map to map every element of the list to an integer value
print(maximum_n(num))