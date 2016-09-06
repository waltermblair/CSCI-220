import math

def getNumbers():
    nums=[]

    xStr=input("Enter a number (<Enter> to quit) >> ")
    while xStr != "":
        x=eval(xStr)
        nums.append(x)
        xStr=input("Enter a number (<Enter> to quit) >> ")
    return nums

def mean(nums):
    sum=0.0
    for x in nums:
        sum=sum+x
    return sum/len(nums)

def stdev(nums,avg):
    sumDevSq=0.0
    for num in nums:
        dev = avg-num
        sumDevSq=sumDevSq+dev**2
    return math.sqrt(sumDevSq/len(nums)-1)

def median(nums):
    nums.sort()
    if len(nums)%2==0:
        return (nums[len(nums)//2-1]+nums[len(nums)//2+1])/2
    else:
        return nums[len(nums)//2]

def main():
    data=getNumbers()
    print("The mean is ",mean(data))
    print("The standard deviation is ",stdev(data,mean(data)))
    print("The median is ",median(data))

if __name__=="__main__": main()
