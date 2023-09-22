with open('day9.txt') as f:
    read_data = f.read().strip().split('\n')
    nums = [int(i) for i in read_data]
    print(nums)

# Part 1
def find_error(nums):
    for i in range(25, len(nums)):
        check = nums[i-25:i]
        if all(nums[i] - n not in check for n in check):
            return nums[i]

error = find_error(nums)
print(error)


# Part 2
def find_encryption_weakness(nums, error):
    for i in range(len(nums)):
        nums_lst = []
        for j in range(i, len(nums)):
            nums_lst.append(nums[j])
            if sum(nums_lst) == error:
                return min(nums_lst) + max(nums_lst)
            elif sum(nums_lst) > error:
                break

print(find_encryption_weakness(nums, error))