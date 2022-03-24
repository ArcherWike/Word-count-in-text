signs = [';', ',', '.', ':']

count_line = 0
count_word = 0

with open('pt1.txt', 'r') as file:
    while True:
        line = file.readline()
        if not line:
            break
        spaced_line = line.split()
        found_word = 0
        for word in spaced_line:
            if len(word) >= 8 and word.count('a') >= 2:
                if word[-1] in signs:
                    if len(word)-1 == 8:
                        found_word += 1
                elif len(word) == 8:
                    found_word += 1
        if found_word >= 1:
            count_word += found_word
            count_line += 1
            print(line, end='')
print(count_line, count_word)

