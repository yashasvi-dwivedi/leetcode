from collections import defaultdict


class Solution(object):
    def largestPathValue(self, colors, edges):
        INF = float("inf")  # Used to indicate a cycle
        n = len(colors)
        adj = defaultdict(list)  # Adjacency list for the graph
        for u, v in edges:
            adj[u].append(v)

        count = [[0] * 26 for _ in range(n)]  # count[i][c]: max count of color c in any path starting at node i
        vis = [0] * n  # 0: unvisited, 1: visiting, 2: visited

        def dfs(node):
            if vis[node] == 1:
                # Found a cycle
                return INF
            if vis[node] == 2:
                # Already computed for this node, return the color count for this node's color
                return count[node][ord(colors[node]) - ord("a")]

            vis[node] = 1  # Mark as visiting
            for nxt in adj[node]:
                res = dfs(nxt)
                if res == INF:
                    # Cycle detected in recursion
                    return INF
                # Update color counts for all colors based on child nodes
                for c in range(26):
                    count[node][c] = max(count[node][c], count[nxt][c])

            col = ord(colors[node]) - ord("a")  # Current node's color index
            count[node][col] += 1  # Include this node's color
            vis[node] = 2  # Mark as visited

            return count[node][col]  # Return the max color count for this node's color

        ans = 0  # Store the answer (max color value along any path)
        for i in range(n):
            val = dfs(i)
            if val == INF:
                # If a cycle is detected, return -1
                return -1
            ans = max(ans, val)  # Update the answer if needed

        return ans  # Return the largest color value found


# Test Cases
if __name__ == "__main__":
    colors = "abaca"
    edges = [[0, 1], [0, 2], [2, 3], [3, 4]]
    s = Solution()
    result = s.largestPathValue(colors, edges)
    print(result)  # Output = 3
