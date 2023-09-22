with open('day6.txt') as f:
    read_data = f.read().strip().split('\n\n')
    processed_data = [_.split('\n') for _ in read_data]
    print(processed_data)

# Part 1
yes_answers = [[i for j in k for i in j] for k in processed_data]
print(yes_answers)
yes_questions = [len(set(_)) for _ in yes_answers]
print(sum(yes_questions))

# Part 2
unified_answers = []
for i in range(len(processed_data)):
    # if len(processed_data[i]) == 1:
    #     unified_answers.append(len(yes_answers[i]))
    # elif len(set(yes_answers[i])) == 1:
    #     unified_answers.append(1)
    answers = {}
    for j in processed_data[i]:
        for k in j:
            if k not in answers:
                answers[k] = 1
            else:
                answers[k] += 1
    # print(answers)
    for a in answers:
        if answers[a] == len(processed_data[i]):
            unified_answers.append(a)

print(len(unified_answers))
