with open('24средняя.txt', 'r') as file:
    s = file.read().strip()

count = 0

for i in range(len(s) - 11):
    if s[i] == 'S':
        for j in range(i + 11, len(s)):
            if s[j] == 'S' and 'S' not in s[i + 1:j]:
                count += 1
                break

print(count)

