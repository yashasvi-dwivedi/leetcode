from typing import List


class Solution:
    def productQueries(self, num: int, queries: List[List[int]]) -> List[int]:
        powList = []
        while num:
            lowBit = num & -num
            powList.append(lowBit)
            num ^= lowBit

        size = len(powList)
        prodTable = [[0] * size for _ in range(size)]
        for row, val in enumerate(powList):
            prodTable[row][row] = val
            for col in range(row + 1, size):
                prodTable[row][col] = (
                    prodTable[row][col - 1] * powList[col] % (10**9 + 7)
                )

        return [prodTable[p][q] for p, q in queries]


# Test cases
print(Solution().productQueries(5, [[0, 0], [0, 1], [1, 1]]))
print(Solution().productQueries(3, [[0, 0], [0, 1], [1, 1]]))
print(Solution().productQueries(7, [[0, 0], [0, 1], [1, 1]]))
print(Solution().productQueries(2, [[0, 0]]))
