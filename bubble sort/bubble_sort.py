import random


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

def bub_sort_by(nums, key):
    for i in range(len(nums)-1):
        swapped = False
        for j in  range(len(nums)-1-i):
            if nums[j][key]>nums[j+1][key]:
                temp=nums[j]
                nums[j]=nums[j+1]
                nums[j+1]=temp
                swapped=True
        if not swapped :
            break
    return nums

if __name__ == '__main__':
    nums=[random.randint(0,1000) for i in range(1000)]
    sorted=bub_sort(nums)
    print(sorted[500:520])

    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    sorted=bub_sort_by(elements, 'device')
    print(sorted)