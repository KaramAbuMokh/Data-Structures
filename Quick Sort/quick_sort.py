import random


def part(nums,left,right):
    pivind=left
    piv=nums[pivind]
    while left<right:
        while left<len(nums)and piv>=nums[left]:
            left+=1
        while nums[right]>piv:
            right-=1
        if left < right:
            temp=nums[right]
            nums[right]=nums[left]
            nums[left]=temp

    temp = nums[right]
    nums[right] = nums[pivind]
    nums[pivind] = temp
    return right



def q_sort(nums,left,right):
    if left<right:
        pi=part(nums,left,right)
        q_sort(nums, left, pi - 1)
        q_sort(nums, pi + 1, right)


def lomuto(nums,left,right):
    if left>=right:
        return
    p_index=i=left
    pivotindex=right
    piv=nums[pivotindex]
    while i<=pivotindex :
        while p_index<pivotindex and nums[p_index]<=piv:
            p_index+=1
        i=p_index
        while nums[i] > piv:
            i+= 1
        temp = nums[p_index]
        nums[p_index] = nums[i]
        nums[i] = temp
        if i==pivotindex:
            break

    lomuto(nums, left, p_index - 1)
    lomuto(nums, p_index + 1, right)


if __name__ == '__main__':
    nums=[random.randint(0,40) for i in range(30)]
    lomuto(nums,0,len(nums)-1)
    print(nums)