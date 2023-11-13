nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2

# for i in range(0, len(nums)):
#     if nums[i] == val:
while val in nums:
    nums.remove(val)

print(nums)
print(len(nums))
