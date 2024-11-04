class Solution(object):
    def merge(self, nums1, m, nums2, n):

        nums1[m:] = nums2[:n]
        nums1.sort()
        
        nums1[:] = [x for x in nums1 if x != 0]
        
        print(nums1)
