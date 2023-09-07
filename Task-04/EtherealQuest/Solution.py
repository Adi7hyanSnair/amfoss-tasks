# Read the number of force vectors
n = int(input())

# Initialize variables to store the resultant force vector
resultant_force = [0, 0, 0]

# Loop through the force vectors and calculate the resultant force
for _ in range(n):
    x, y, z = map(int, input().split())
    resultant_force[0] += x
    resultant_force[1] += y
    resultant_force[2] += z

# Check if the resultant force is (0, 0, 0) and print the result
if resultant_force == [0, 0, 0]:
    print("YES")
else:
    print("NO")
