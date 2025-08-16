class Solution:
    def maximum69Number(self, num: int) -> int:
        tens = (1000, 100, 10, 1)
        for t in tens:
            r = num // t % 10
            if r == 6:
                return num + 3 * t
        return num


if __name__ == "__main__":
    sol = Solution()
    print(sol.maximum69Number(9669))  # Output: 9969
    print(sol.maximum69Number(9996))  # Output: 9999
    print(sol.maximum69Number(9999))  # Output: 9999ds
