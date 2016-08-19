# P12 2.1-1
def insert_sort(nums, isIncrease=1):
    if isIncrease:
        for j in range(1, len(nums)):
            key = nums[j]
            i = j-1
            while i>-1 and nums[i]>key:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = key
        return nums
    else:
        for j in range(1, len(nums)):
            key = nums[j]
            i = j-1
            while i>-1 and nums[i]<key:
                nums[i+1] = nums[i]
                i -= 1
            nums[i+1] = key
        return nums

# P12 2.1-3
def search_num(nums, val):
    idx = []
    for i in range(len(nums)):
        if nums[i]==val:
            idx.append(i)
    return idx

# P12 2.1-4
def add_binary(A, B):
    C = [0 for i in range(len(A)+1)]
    flag = 0
    for i in range(len(A)):
        if A[i]+B[i]+flag==2:
            C[i] = 0
            flag = 1
        elif A[i]+B[i]+flag==1:
            C[i] = 1
            flag = 0
        elif A[i]+B[i]+flag==3:
            C[i] = 1
            flag = 1
        else:
            C[i] = 0
            flag = 0
    C[-1] = flag
    return C



if __name__ == '__main__':
    nums = [2,1,5,6,8]
    print insert_sort(nums, isIncrease=1)
    print search_num(nums, 8)
    print add_binary([1,0,0,1],[1,1,1,1])