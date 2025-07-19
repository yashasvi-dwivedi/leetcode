class Solution:
    def removeSubfolders(self, folder):
        folder.sort()
        res = []
        for f in folder:
            if not res:
                res.append(f)
            else:
                prev = res[-1]
                if f.startswith(prev) and len(f) > len(prev) and f[len(prev)] == "/":
                    continue
                else:
                    res.append(f)
        return res


# Test cases
if __name__ == "__main__":
    solution = Solution()
    print(solution.removeSubfolders(["/a", "/a/b", "/c/d", "/c/d/e"]))
    print(solution.removeSubfolders(["/a/b/c", "/a/b/d", "/a/b/c/d"]))
    print(solution.removeSubfolders(["/x/y/z", "/x/y/z/a", "/x/y"]))
