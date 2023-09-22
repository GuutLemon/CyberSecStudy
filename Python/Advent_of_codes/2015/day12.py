def unpack_numbers(data, num_lst=[]):
    if isinstance(data, int):
        num_lst.append(data)
    elif isinstance(data, list):
        for i in data:
            unpack_numbers(i, num_lst)
    elif isinstance(data, dict):

        ###### Part 2
        if 'red' in data.values():
            return
        #########

        for value in data.values():
            unpack_numbers(value, num_lst)
    return num_lst

with open('day12.txt') as f:
    read_data = f.read().strip()
    #print(read_data)
    print(sum(unpack_numbers(eval(read_data))))

# a = [{'a': [4, 6, {'b': {'f': [5,7,8]}}], 'z': ['f', 4]}]
# print(unpack_numbers(a))