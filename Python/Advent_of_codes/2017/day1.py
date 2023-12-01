with open("day1.txt") as f:
    numlst = [int(i) for i in f.read()]


def solve_captcha(numlst, steps):
    matched_nums = []
    for i, n in enumerate(numlst):
        pos = (i + steps) % len(numlst)
        if n == numlst[pos]:
            matched_nums.append(n)
    return sum(matched_nums)

# Part 1
print(solve_captcha(numlst, 1))

# Part 2
print(solve_captcha(numlst, len(numlst)//2))
