a = int(input("Enter the start value (in integer):"))
b = int(input("Enter the end value (in integer):"))
b = b+1
prime = 0
composite_numbers = 0
even = 0
odd = 0
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def is_even(n):
    return n % 2 == 0
# the return value is in boolean ether way

for num in range(a,b):
    if num>1:
        if is_prime(num):
            prime+=1
        else:
            composite_numbers+=1
    if is_even(num):
        even += 1
    else:
        odd += 1
print(f"There are a total of '{prime}' prime numbers in between {a} and {b-1}.")
print(f"There are a total of '{composite_numbers}' composite numbers in between {a} and {b-1}.")
print(f"There are a total of '{even}' even numbers in between {a} and {b-1}.")
print(f"There are a total of '{odd}' odd numbers in between {a} and {b-1}.")