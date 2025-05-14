class Solution(object):
    mod = 10**9 + 7

    def multiplyMatrices(self, A, B):
        rowsA, colsA, colsB = len(A), len(A[0]), len(B[0])
        result = [[0] * colsB for _ in range(rowsA)]
        for i in range(rowsA):
            for j in range(colsB):
                tmp = 0
                for k in range(colsA):
                    tmp = (tmp + A[i][k] * B[k][j]) % self.mod
                result[i][j] = tmp
        return result

    def powerMatrix(self, matrix, exponent):
        n = len(matrix)
        result = [[1 if i == j else 0 for j in range(n)] for i in range(n)]
        while exponent > 0:
            if exponent & 1:
                result = self.multiplyMatrices(result, matrix)
            matrix = self.multiplyMatrices(matrix, matrix)
            exponent >>= 1
        return result

    def lengthAfterTransformations(self, s, t, nums):
        # Updated to support multiple transitions per step
        transform = [[0] * 26 for _ in range(26)]
        for i in range(26):
            for shift in range(1, nums[i] + 1):
                transform[i][(i + shift) % 26] += 1

        # Simulate t transformations
        transform = self.powerMatrix(transform, t)

        # Initialize frequency vector from input string
        freq = [[0] * 26]
        for ch in s:
            freq[0][ord(ch) - ord("a")] += 1

        # Apply transformation
        freq = self.multiplyMatrices(freq, transform)

        return sum(freq[0]) % self.mod


# Test the function
if __name__ == "__main__":
    solution = Solution()
    s = "abc"
    t = 2
    nums = [
        1,
        2,
        3,
        4,
        5,
        6,
        7,
        8,
        9,
        10,
        11,
        12,
        13,
        14,
        15,
        16,
        17,
        18,
        19,
        20,
        21,
        22,
        23,
        24,
        25,
    ]
    result = solution.lengthAfterTransformations(s, t, nums)
    print(result)  # Expected output: some integer
