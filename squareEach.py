nums=[2,4,6,8]

def squareEach(nums):
    for i in range(len(nums)):
        nums[i]=nums[i]**2
    return nums

def sumList(nums):
    mysum=0
    for i in range(len(nums)):
        mysum=mysum+nums[i]
    return mysum

def main():
    squareEach(nums)
    print(nums)
    print("Sum = {0}".format(sumList(nums)))
main()
