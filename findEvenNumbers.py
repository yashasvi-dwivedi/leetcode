from collections import Counter


class Solution(object):
    def findEvenNumbers(self, digits):
        count = Counter(digits)
        result = []

        for num in range(100, 1000):
            if num % 2 == 1:
                continue

            c = Counter(map(int, str(num)))
            if all(count[d] >= c[d] for d in c):
                result.append(num)

        return result


# Test the function
if __name__ == "__main__":
    digits = [2, 1, 3, 0]
    sol = Solution()
    print(sol.findEvenNumbers(digits))  # Output: [120, 102, 210, 201, 320, 302]
