class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        len_nums = len(nums)
        if not len_nums:
            return 0
        j = 1
        for i in range(len_nums-1):
            if nums[j] == nums[j-1]:
                _ = nums.pop(j)
            else:
                j += 1
        return j



if __name__ == '__main__':
    test = Solution()
    nums = []
    print test.removeDuplicates(nums)
