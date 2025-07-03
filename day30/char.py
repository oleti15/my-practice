def alternating_subarray(nums):
    n = len(nums)
    max_len = -1

    for i in range(n - 1):
        if nums[i + 1] - nums[i] == 1:
            length = 2
            expected = -1 
            for j in range(i + 1, n - 1):
                if nums[j + 1] - nums[j] == expected:
                    length += 1
                    expected *= -1  
                else:
                    break
            max_len = max(max_len, length)

    return max_len
nums=[2,3,4,3,4]
print(alternating_subarray(nums))