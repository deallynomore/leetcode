class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """
        i = 0
        j = 0

        while 1:


            if nums1[i] < nums2[j]:
                i += 1
            else:
                nums1.insert(i,nums2[j])
                j += 1



