import re

# Part 1
# Regex practice
# def find_marker(data):
#     pattern = r"((\w)(?!\2)(\w)(?!\2|\3)(\w)(?!\2|\3|\4)(\w))"
#     matches = re.findall(pattern, data)
#     results = [match[0] for match in matches]
#     result = results[0]
#     print(result)
#     for i in range(len(data)):
#         if data[i:i+4] == result:
#             print(data[i:i+4])
#             return i + 4

# Part 2
def find_marker(data):
    for i in range(len(data)):
        if len(list(set(data[i:i+14]))) == 14 and i < len(data) - 14:
            return i + 14


with open('day6.txt') as f:
    read_data = f.read().strip()
    print(find_marker(read_data))