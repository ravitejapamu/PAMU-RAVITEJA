#Problem-2 (Series Generation - Odd Numbers): Generate a series of odd numbers up to a specified limit.
#Accept a single integer a as input.
#Generate a series of odd numbers starting from 1, incrementing by 2 in each step.
#Continue generating numbers until the number of generated odd numbers equals a.
#Output the generated series as a comma-separated string.


def generate_odd_series(a):
    if a <= 0:
        return ""
    
    odd_numbers = []
    current = 1
    for _ in range(a):
        odd_numbers.append(current)
        current += 2
    
    return ",".join(map(str, odd_numbers))

# Input
a = int(input("Enter the number of odd numbers to generate: "))
# Output
print(generate_odd_series(a))