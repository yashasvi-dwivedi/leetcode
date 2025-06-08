class Solution(object):
    def lexicalOrder(self, n):
        result = []

        def dfs(current):
            if current > n:
                return
            result.append(current)
            for i in range(10):
                next_num = current * 10 + i
                if next_num > n:
                    break
                dfs(next_num)

        for i in range(1, 10):
            dfs(i)

        return result


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.lexicalOrder(13))  # Output: [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
