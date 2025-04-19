#Problem-3 (Series Generation - Selective Odd Numbers): Generate a series of odd numbers selectively based on the input.
#Accept a single integer a as input.
#If a is even, generate odd numbers until a/2 numbers is equal to x, then output series (1,3,5,7,9…)
#If a is odd, generate odd numbers until (a+1)/2 numbers is equal to x, then output series (1,3,5,7,9…)
#Output the generated series as a comma-separated string.

# Function to generate selective odd numbers series
def generate_odd_series(a):
    if a % 2 == 0:
        x = a // 2
    else:
        x = (a + 1) // 2

    # Generate the series of odd numbers
    series = [str(2 * i + 1) for i in range(x)]
    return ",".join(series)

# Input from the user
try:
    a = int(input("Enter an integer: "))
    if a < 0:
        print("Please enter a non-negative integer.")
    else:
        result = generate_odd_series(a)
        print("Generated series:", result)
except ValueError:
    print("Invalid input. Please enter an integer.");