def can_say_hello(s):
    target = "hello"
    i = 0  # Index for the target word
    
    for char in s:
        if char == target[i]:
            i += 1
            if i == len(target):
                return "YES"  # Alex successfully said "hello"
    
    return "NO"  # Alex couldn't say "hello" correctly

# Read input
s = input().strip()

# Check if Alex can say "hello"
result = can_say_hello(s)
print(result)
