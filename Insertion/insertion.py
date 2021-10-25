import random


def ins(nums):
    new_len=0
    for not_sorted_index in range(1,len(nums)):
        new_len += 1
        for sorted_index in range(new_len):
            if nums[sorted_index]>nums[not_sorted_index]:
                nums.insert(sorted_index, nums[not_sorted_index])
                del nums[not_sorted_index+1]
                new_len+=1
                break

def ins2(nums):
    for not_sorted_index in range(1,len(nums)):
        sorted_index=not_sorted_index-1
        temp = nums[not_sorted_index]
        while sorted_index>=0 and nums[sorted_index]>temp :
            nums[sorted_index + 1] = nums[sorted_index]
            sorted_index-=1
        nums[sorted_index+1]=temp


if __name__ == '__main__':
    nums=[random.randint(0,100) for i in range(20)]
    ins2(nums)
    print(nums)