nums = [1,2,3,4,5,6,7,8]
input = 1

def binary_search(nums: list, input):
    n = len(nums)
    if n % 2 == 1:
        p = int((n - 1) / 2)
        mid = nums[p]
        # print(mid)
        left = (nums[0:p])
        right = (nums[p + 1:])
        print (left,mid,right)

        if input == mid:
            return True
        elif input > mid:
            binary_search(nums=right, input=input)
        else:
            binary_search(nums=left, input=input)
    else:
        p = int(n / 2) 
        mid1 = nums[p-1]
        mid2 = nums[p]
        # p = p - 1
        # print(mid1, mid2)
        left = (nums[0:p-1])
        right = (nums[p + 1:])
        print (left,mid1,mid2,right,)

        if (input == mid1) or (input == mid2):
            return True
        elif input > mid2:
            binary_search(nums=right, input=input)
        else:
            binary_search(nums=left, input=input)

result = binary_search(nums=nums, input=input)
print(result)