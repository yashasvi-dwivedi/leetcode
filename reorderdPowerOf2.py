from collections import Counter


class Solution(object):
    def reorderedPowerOf2(self, n):
        return Counter(str(n)) in (Counter(str(1 << i)) for i in range(30))


if __name__ == "__main__":
    print("Provide a value for n: ")
    n = int(input())
    print(Solution().reorderedPowerOf2(n))
