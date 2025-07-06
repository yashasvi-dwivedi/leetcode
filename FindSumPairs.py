from collections import Counter


class FindSumPairs:
    def __init__(self, nums1, nums2):
        self.nums1 = nums1
        self.nums2 = nums2
        self.nums2_count = Counter(nums2)

    def add(self, index: int, val: int) -> None:
        self.nums2_count[self.nums2[index]] -= 1
        if self.nums2_count[self.nums2[index]] <= 0:
            self.nums2_count.pop(self.nums2[index])

        self.nums2[index] += val
        self.nums2_count[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        count = 0
        for val in self.nums1:
            count += self.nums2_count[tot - val]
        return count


# Test cases
if __name__ == "__main__":
    fsp = FindSumPairs([1, 2, 3], [4, 5, 6])
    print(fsp.count(7))  # Output: 3 (1+6, 2+5, 3+4)
    fsp.add(0, 1)  # nums2 becomes [5, 5, 6]
    print(fsp.count(7))  # Output: 2 (2+5, 3+4)
    fsp.add(1, -1)  # nums2 becomes [5, 4, 6]
    print(fsp.count(7))  # Output: 3 (1+6, 2+5, 3+4)
