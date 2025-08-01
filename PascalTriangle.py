class Solution:
    def PascalTriangle(self, numRows):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]

        prevRows = self.PascalTriangle(numRows - 1)
        newRow = [1] * numRows

        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]

        prevRows.append(newRow)
        return prevRows


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.PascalTriangle(5))
    print(sol.PascalTriangle(0))
    print(sol.PascalTriangle(1))
    print(sol.PascalTriangle(2))
