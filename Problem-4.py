#Problem-4 (Dictionary Count of Multiples): Count the number of elements in a list that are multiples of numbers from 1 to 9.
#Accept a list of integers as input.
#Create a dictionary with keys from 1 to 9.
#Iterate through the input list.
#For each number in the list, check if it is a multiple of each number from 1 to 9.
#If it is a multiple, increment the corresponding count in the dictionary.
#Output the dictionary.


def count_multiples(input_list):
    # Initialize dictionary for counts of multiples of 1 to 9
    multiples_count = {i: 0 for i in range(1, 10)}
    
    # Iterate through the list of integers provided as input
    for num in input_list:
        # Check divisibility for each key in the dictionary (1 to 9)
        for i in range(1, 10):
            if num % i == 0:  # If divisible, increment the count
                multiples_count[i] += 1
    
    return multiples_count

# Accepting input from the user
input_list = list(map(int, input("Enter a list of integers separated by spaces: ").split()))
output = count_multiples(input_list)
print("Output:", output)
