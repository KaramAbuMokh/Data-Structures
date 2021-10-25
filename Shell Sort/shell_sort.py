import random


def shell_s(nums):
    size = len(nums)
    gap=size//2
    while gap>0:

        for i in range(gap,size):
            temp=nums[i]
            j=i
            while j>=gap and nums[j-gap]>temp:
                nums[j]=nums[j-gap]
                j-=gap
            nums[j]=temp
        gap=gap//2

def shell_s_unique(nums):

    div=2
    size = len(nums)
    gap=size//div
    while gap>0:
        todel = []
        for i in range(gap,size):
            temp=nums[i]
            j=i
            while j>=gap and nums[j-gap]>=temp:
                if nums[j-gap]==temp:
                    todel.append(j)
                nums[j]=nums[j-gap]
                j-=gap

            nums[j]=temp
        todel = list(set(todel))
        todel.sort()
        if todel:
            for i in todel[::-1]:
                del nums[i]
        size = len(nums)
        div*=2
        gap=size//div

if __name__ == '__main__':

    nums=[random.randint(0,10) for i in range(10)]
    print(nums)
    shell_s_unique(nums)
    print(nums)