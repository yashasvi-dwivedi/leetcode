from collections import defaultdict


class Solution(object):
    def twoSum(self, numbers, target):
        mp = defaultdict(int)
        for i in range(len(numbers)):
            tmp = target - numbers[i]
            if mp[tmp]:
                return [mp[tmp], i + 1]
            mp[numbers[i]] = i + 1
        return []


# Test the function
if __name__ == "__main__":
    solution = Solution()
    numbers = [2, 7, 11, 15]
    target = 9
    result = solution.twoSum(numbers, target)
    print(result)  # Expected output: [1, 2]
    solution = Solution()
    numbers = [3, 2, 4]
    target = 6
    result = solution.twoSum(numbers, target)
    print(result)  # Expected output: [2, 3]
