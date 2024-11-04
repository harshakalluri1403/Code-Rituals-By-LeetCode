class Solution(object):
    def merge(self, nums1, m, nums2, n):

        nums1[m:] = nums2[:n]
        nums1.sort()
        
        # Now remove any remaining zeros from the sorted array (if there are any)
        nums1[:] = [x for x in nums1 if x != 0]
        
        print(nums1)
