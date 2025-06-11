import sys


class Solution:
    def maxDifference(self, s: str, k: int) -> int:
        n = len(s)
        ans = -sys.maxsize

        # Helper function to get the 2-bit parity state
        def getStatus(cnt_a, cnt_b):
            return ((cnt_a & 1) << 1) | (cnt_b & 1)

        # Iterate through all possible pairs of distinct characters (a, b)
        for a in map(str, range(5)):
            for b in map(str, range(5)):
                if a == b:
                    continue

                best = [sys.maxsize] * 4
                best[getStatus(0, 0)] = 0  # Initialize for the prefix before the string
                cnt_a = cnt_b = 0
                prev_a = prev_b = 0
                left = -1

                for right in range(n):
                    cnt_a += s[right] == a
                    cnt_b += s[right] == b

                    # Move left pointer and update best array
                    while right - left >= k and cnt_b - prev_b >= 2:
                        left_status = getStatus(prev_a, prev_b)
                        best[left_status] = min(best[left_status], prev_a - prev_b)
                        left += 1
                        prev_a += s[left] == a
                        prev_b += s[left] == b

                    right_status = getStatus(cnt_a, cnt_b)
                    required_status = right_status ^ 0b10

                    if best[required_status] != sys.maxsize:
                        ans = max(ans, cnt_a - cnt_b - best[required_status])

        return ans if ans != -sys.maxsize else -1


# Test Cases
if __name__ == "__main__":
    sol = Solution()
    print(sol.maxDifference("00110011", 2))  # Example test case
    print(sol.maxDifference("1100", 1))      # Another test case
    print(sol.maxDifference("101010", 3))    # Yet another test case
