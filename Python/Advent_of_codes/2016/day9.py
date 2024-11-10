def decompress(input):
    wait = False
    seq_length = 0
    closed_marker = True
    decompressed = ''
    for i in range(len(input)):
        if input[i] == '(' and not wait:
            marker = ''
            wait = True
            closed_marker = False
        elif input[i] != ')' and wait and not closed_marker:
            marker += input[i]
        elif input[i] == ')' and wait and not closed_marker:
            closed_marker = True
            marker = marker.split('x')
            seq_length = i + int(marker[0]) + 1
            repeat = int(marker[1])
            decompressed += input[i+1:seq_length] * repeat
        elif i == seq_length - 1 and wait:
            wait = False
        elif not wait:
            decompressed += input[i]
    return decompressed


def full_decom(input):
    leng = 0
    i = 0
    if '(' not in input:
        return len(input)
    while i < len(input):
        start_marker = input.find('(', i)
        end_marker = input.find(')', i)
        leng += start_marker - i
        marker = input[start_marker+1:end_marker].split('x')
        seq_length = end_marker + int(marker[0])
        repeat = int(marker[1])
        recur_input = input[end_marker + 1:seq_length + 1] * repeat
        leng += full_decom(recur_input)
        i = seq_length
        i += 1
    return leng


if __name__ == '__main__':
    with open('day9.txt') as f:
        data = f.read().strip().strip(' ')

    decom = decompress(data)
    print('Part 1: ', len(decom))
    print('Part 2: ', full_decom(decom))

