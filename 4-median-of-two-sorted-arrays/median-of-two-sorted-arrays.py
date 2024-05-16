class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        # Merge the two arrays and sort them
        merged = nums1 + nums2
        merged.sort()
        n = len(merged)

        # Handle the case when the merged array is empty
        if n == 0:
            return 0.0

        # Calculate the median
        if n % 2 == 0:
            mid1 = merged[n // 2 - 1]
            mid2 = merged[n // 2]
            median = (mid1 + mid2) / 2.0
        else:
            median = merged[n // 2]

        return median