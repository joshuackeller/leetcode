class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        half = ((len(nums1) + len(nums2)) // 2)
        use_two_values = (len(nums1) + len(nums2)) / 2 == (len(nums1) + len(nums2)) // 2

        p1, p2, n1, n2 = 0, 0, 0, 0

        for _ in range(half + 1):
            n2 = n1
            if p2 == len(nums2) or (p1 < len(nums1) and nums1[p1] < nums2[p2]):
                n1 = nums1[p1]
                p1 += 1
            else:
                n1 = nums2[p2]
                p2 += 1

        if use_two_values:
            return (n1 + n2) / 2
        else:
            return n1
