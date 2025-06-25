class Solution(object):
    def kthSmallestProduct(self, nums1, nums2, k):
        nums1.sort()
        nums2.sort()

        def count_pairs(x):
            count = 0
            for a in nums1:
                if a > 0:
                    count += bisect.bisect_right(nums2, x // a)
                elif a < 0:
                    target = x // a
                    if x % a != 0:
                        target += 1
                    count += len(nums2) - bisect.bisect_left(nums2, target)
                else:
                    if x >= 0:
                        count += len(nums2)

            return count

        low = -(10**10)
        high = 10**10

        while low < high:
            mid = (low + high) // 2
            if count_pairs(mid) < k:
                low = mid + 1
            else:
                high = mid

        return low
