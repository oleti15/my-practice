
nums=[1,2,3,4,5]
target=5
x,y = 0, len(nums) - 1
    
while x <= y:
    mid=(x+y)//2
        
    if nums[mid] == target:
        print(mid)
    elif nums[mid] < target:
        x = mid + 1
    else:
         y = mid - 1
    
print(x)   