with open('24легкая.txt', 'r') as file:
    s = file.readline().strip()

max_count = 0
current_count = 0

for char in s:
    if char == 'C':
        current_count += 1
    else:
        max_count = max(max_count, current_count)
        current_count = 0

max_count = max(max_count, current_count)
print(max_count)
