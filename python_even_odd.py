
def print_even_numbers(limit):
    for num in range(0, limit + 1, 2):
        print(num)

def print_odd_numbers(limit):
    for num in range(1, limit + 1, 2):
        print(num)

print("Even Numbers:")
print_even_numbers(100)

print("\nOdd Numbers:")
print_odd_numbers(100)
