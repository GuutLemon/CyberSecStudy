inp = '1113222113'

for _ in range(50):
    count = 1
    result = ''
    for i, j in enumerate(inp):
        if i < len(inp) - 1:
            if inp[i] == inp[i+1]:
                count += 1
            else:
                result += str(count) + j
                count = 1
        elif i == len(inp) - 1:
            result += str(count) + j
    inp = result
    print(_)

print(len(result))