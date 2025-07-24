class Solution(object):
    def minimumScore(self, nums, edges):
        from collections import defaultdict
        import sys

        sys.setrecursionlimit(10000)

        n = len(nums)
        graph = defaultdict(list)
        for u, v in edges:
            graph[u].append(v)
            graph[v].append(u)

        subXor = [0] * n
        inTime = [0] * n
        outTime = [0] * n
        time = [0]

        def dfs(u, parent):
            inTime[u] = time[0]
            time[0] += 1
            xorVal = nums[u]
            for v in graph[u]:
                if v != parent:
                    xorVal ^= dfs(v, u)
            subXor[u] = xorVal
            outTime[u] = time[0]
            time[0] += 1
            return xorVal

        dfs(0, -1)
        totalXor = subXor[0]

        def isAncestor(u, v):
            return inTime[u] <= inTime[v] and outTime[v] <= outTime[u]

        res = float("inf")

        # 枚舉所有邊組合，邊代表其連接的兩個節點 (保證有方向)
        edgeList = []
        for u, v in edges:
            if inTime[u] > inTime[v]:
                u, v = v, u
            edgeList.append(v)  # 儲存子節點方向

        for i in range(len(edgeList)):
            for j in range(i + 1, len(edgeList)):
                a = edgeList[i]
                b = edgeList[j]

                if isAncestor(a, b):
                    xor1 = subXor[b]
                    xor2 = subXor[a] ^ subXor[b]
                    xor3 = totalXor ^ subXor[a]
                elif isAncestor(b, a):
                    xor1 = subXor[a]
                    xor2 = subXor[b] ^ subXor[a]
                    xor3 = totalXor ^ subXor[b]
                else:
                    xor1 = subXor[a]
                    xor2 = subXor[b]
                    xor3 = totalXor ^ subXor[a] ^ subXor[b]

                values = [xor1, xor2, xor3]
                res = min(res, max(values) - min(values))

        return res


# Test cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.minimumScore([1, 2, 3], [[0, 1], [1, 2]]))  # Output: 0
    print(sol.minimumScore([5, 6, 7], [[0, 1], [1, 2]]))  # Output: 0
    print(sol.minimumScore([1, 2, 3, 4], [[0, 1], [1, 2], [2, 3]]))  # Output: 0
    print(sol.minimumScore([10, 20, 30], [[0, 1], [1, 2]]))  # Output: 0
