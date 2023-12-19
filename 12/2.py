from functools import cache


def count(pattern, nums):
    m, n = len(pattern), len(nums)

    @cache
    def helper(i, j):
        if j == n:
            return 1 if '#' not in pattern[i:] else 0
        cur = nums[j]
        if i + cur > m:
            return 0

        ret = 0
        if pattern[i] != '#':
            ret += helper(i+1, j)
        if (
            '.' not in pattern[i:i+cur] and
            '#' not in pattern[i+cur:i+cur+1]
        ):
            ret += helper(i + cur + 1, j + 1)
        return ret

    return helper(0, 0)


tot = 0
with open('1.2.in') as file:
    for line in file:
        pattern, nums = line[:-1].split(' ')
        pattern = '?'.join([pattern] * 5)
        nums = [int(x) for x in nums.split(',')] * 5
        tot += count(pattern, nums)
        print(tot)
