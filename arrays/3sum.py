"""
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.
Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.
Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.
"""
nums = [-1, 0, 1, 2, -1, -4]

output = []


# for i in range(0, len(nums) - 2):
#     for j in range(i + 1, len(nums) - 1):
#         for k in range(j + 1, len(nums)):
#             temp = []
#             if i != j != k and nums[i] + nums[j] + nums[k] == 0:
#                 temp.append(nums[i])
#                 temp.append(nums[j])
#                 temp.append(nums[k])
#                 temp.sort()
#                 if temp not in output:
#                     output.append(temp)

# print(output)
# t_list = []
# for i in range(0, len(nums) - 1):
#     for j in range(i + 1, len(nums)):
#         t_sum = nums[i] + nums[j]
#         if -t_sum in nums:
#             if -t_sum not in [nums[i], nums[j]]:
#                 t_list = [nums[i], nums[j], -t_sum]
#                 # sorted(t_list)
#                 t_list.sort()
#             if t_list not in output:
#                 output.append(t_list)

# print(output)

ans = []
nums.sort()

for i in range(len(nums)):
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    j = i + 1
    k = len(nums) - 1

    while j < k:
        sum = nums[i] + nums[j] + nums[k]

        if sum < 0:
            j += 1
        elif sum > 0:
            k -= 1
        else:
            temp = [nums[i], nums[j], nums[k]]
            ans.append(temp)
            j += 1
            k -= 1

            while j < k and nums[j] == nums[j - 1]:
                j += 1
            while j < k and nums[k] == nums[k + 1]:
                k -= 1
