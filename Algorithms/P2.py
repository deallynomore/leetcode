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


# P16 2.2-2
def select_sort(nums):
    for i in range(len(nums)-1):
        temp = nums[i]
        minise = 10000
        for j in range(i,len(nums)):
            if nums[j]<minise:
                minise = nums[j]
                nums[j] = temp
        nums[i] = minise
    return nums


# P22 2.3-2

def merge(A, p, q, r):
    print A
    L = A[p:q]
    R = A[q:r+1]
    print L
    print R
    i = 0
    j = 0
    for k in range(p, r+1):
        if j >= len(R):
            for t in range(i, len(L)):
                A[k] = L[t]
                k+=1
            return A

        elif i >= len(L):
            for t in range(j, len(R)):
                A[k] = R[t]
                k+=1
            return A

        if L[i]<R[j]:
            A[k] = L[i]
            i+=1
        else:
            A[k] = R[j]
            j+=1

    return A


if __name__ == '__main__':
    A = [2,1,5,5,7,9,6,8,2,4]
    # print insert_sort(nums, isIncrease=1)
    # print search_num(nums, 8)
    # print add_binary([1,0,0,1],[1,1,1,1])
    # print select_sort(nums)
    print merge(A, 3, 6, 7)