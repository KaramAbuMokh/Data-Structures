import random
import time

def time_it(func):
    def wrapper(*args,**kwargs):
        start=time.time()
        result=func(*args,**kwargs)
        end=time.time()
        print(func.__name__ +" took " + str((end-start)*1000) + " mil sec")
        return result
    return wrapper


@time_it
def bin_search(nums, num):
    left=0
    right= len(nums)-1
    mid= (left+right)//2

    while left<=right:
        if nums[mid]==num:
            return mid
        elif num<nums[mid]:
            right=mid-1
            mid= (left+right)//2
        elif num>nums[mid]:
            left=mid+1
            mid = (left + right) // 2
    return -1

def bin_search_rec(nums, num, left, right):
    if left>right:
        return -1
    mid=(left+right)//2
    if nums[mid]==num:
        return mid
    if num<nums[mid]:
        right=mid-1
        return bin_search_rec(nums, num, left, right)
    if num>nums[mid]:
        left=mid+1
        return bin_search_rec(nums, num, left, right)
    return -1


@time_it
def search(nums, num):
    for i,x in enumerate(nums):
        if x==num:
            return i
    return -1


def get_all_indexes(nums,num):
    left = 0
    right = len(nums) - 1
    mid = (left + right) // 2

    while left <= right:
        if nums[mid] == num:
            while nums[left]!=num:
                left+=1
            while nums[right]!=num:
                right-=1
            inds=[i for i in range(left,right+1)]
            return inds
        elif num < nums[mid]:
            right = mid - 1
            mid = (left + right) // 2
        elif num > nums[mid]:
            left = mid + 1
            mid = (left + right) // 2
    return -1

def bub_sort(nums):
    for i in range(len(nums)-1):
        swapped = False
        for j in  range(len(nums)-1-i):
            if nums[j]>nums[j+1]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                swapped=True
        if not swapped :
            break
    return nums

if __name__ == '__main__':
    nums=[i for i in range(1000000)]
    i=bin_search(nums,703145)
    print(i)
    i = search(nums, 703145)
    print(i)
    i = bin_search_rec(nums, 999999,0, len(nums)-1)
    print(i)
    print('-----------------------------------------------')
    nums2 = [random.randint(0, 1000) for i in range(1000)]
    nums3=bub_sort(nums2)
    print('-----------------------------------------------')
    print(nums3[520:540])
    all_indexes=get_all_indexes(nums3,400)
    print(all_indexes)