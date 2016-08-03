class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        len_nums = len(nums)
        i = 0
        if len_nums == 0:
            return 0
        for j in range(len_nums):
            if nums[i]==val:
                nums.append(nums.pop(i))
            else:
                i += 1
        return i



if __name__ == '__main__':
    nums = []
    val = 3
    test = Solution()
    print test.removeElement(nums, val)
