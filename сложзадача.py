def find_max_sequence(filename):
    with open(filename, 'r') as file:
        s = file.read().strip().replace(' ', '')

    max_length = 0
    char_set = set()
    start = 0

    for end in range(len(s)):
        while s[end] in char_set:
            char_set.remove(s[start])
            start += 1

        char_set.add(s[end])

        max_length = max(max_length, end - start + 1)

    return max_length


filename = '24сложная.txt'
print(find_max_sequence(filename))

