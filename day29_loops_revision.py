# Day 29 - Loops Revision

# 1. For loop → print 1 to 5
for i in range(1, 6):
    print(i)

# 2. Continue → skip 3
for i in range(1, 6):
    if i == 3:
        continue
    print(i)

# 3. Break → stop at 4
for i in range(1, 6):
    if i == 4:
        break
    print(i)

# 4. While loop → countdown
count = 5
while count > 0:
    print(count)
    count -= 1
print("Blast Off!")

# 5. Nested Loop → pattern
for i in range(3):
    for j in range(3):
        print("*", end=" ")
    print()

