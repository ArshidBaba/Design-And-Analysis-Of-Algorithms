"""
Kadane's Algorithm for maximum subarray problem is a space  optimized version of a dynamic programming solution.
"""
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

maxSumSoFar = maxSumEndingHere = nums[0]

for i in range(1, len(nums)):
    maxSumEndingHere = max(maxSumEndingHere + nums[i], nums[i])
    if maxSumSoFar < maxSumEndingHere:
        maxSumSoFar = maxSumEndingHere

print(maxSumSoFar)
