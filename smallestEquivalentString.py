class Solution:
    def __init__(self):
        # parent[i] holds the representative (root) of character chr(ord('a') + i)
        self.parent = list(range(26))

    def find(self, x):
        # Path compression
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        ra = self.find(a)
        rb = self.find(b)
        if ra == rb:
            return
        # Always attach the larger root to the smaller root
        if ra < rb:
            self.parent[rb] = ra
        else:
            self.parent[ra] = rb

    def smallestEquivalentString(self, s1, s2, baseStr):
        # Merge equivalent characters from s1 and s2
        for c1, c2 in zip(s1, s2):
            x = ord(c1) - ord("a")
            y = ord(c2) - ord("a")
            self.union(x, y)

        # Build and return the resulting string
        ans = []
        for c in baseStr:
            idx = ord(c) - ord("a")
            root = self.find(idx)
            ans.append(chr(root + ord("a")))
        return "".join(ans)
