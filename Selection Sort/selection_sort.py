import random


def selection_s(nums):
    for i in range(len(nums)):
        min=nums[i]
        ind = i
        for j in range(i+1,len(nums)):
            if nums[j]<min:
                min=nums[j]
                ind=j
        nums[ind]=nums[i]
        nums[i]=min


if __name__ == '__main__':

    nums=[random.randint(0,100) for i in range(20)]
    print(nums)
    selection_s(nums)
    print(nums)