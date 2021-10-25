import random

def merge_sorted_two_arrays(a,b):
    left=right=0
    new_list=[]
    while left<len(a)and right<len(b):
        if a[left]>b[right]:
            new_list.append(b[right])
            right+=1
        else:
            new_list.append(a[left])
            left += 1
    while left<len(a):
        new_list.append(a[left])
        left+=1
    while right<len(b):
        new_list.append(b[right])
        right += 1
    return new_list

def merge_s(nums,left,right):
    if left<right:
        mid=(left+right)//2
        merged_left=merge_s(nums,left,mid)
        merged_right = merge_s(nums, mid+1, right)
        merged=merge_sorted_two_arrays(merged_left,merged_right)
        return merged
    if left==right:
        return [nums[right]]


if __name__ == '__main__':

    nums=[random.randint(0,10) for i in range(5)]
    print(nums)
    merged=merge_s(nums,0,len(nums)-1)
    print(merged)