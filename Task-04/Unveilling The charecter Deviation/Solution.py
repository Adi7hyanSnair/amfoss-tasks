# Function to calculate the number of differing indices
def count_differing_indices(s):
    reference = "amfoss"
    count = 0
    for i in range(len(s)):
        if s[i] != reference[i]:
            count += 1
    return count

# Input the number of test cases
t = int(input())

# Process each test case
for _ in range(t):
    s = input().strip()  # Read the input string
    result = count_differing_indices(s)  # Calculate the number of differing indices
    print(result)  # Output the result for the current test case
