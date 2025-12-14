nums = [1, 2, 3, 4]
# nums = [-1,1,0,-3,3]
answer = []

# Brute force approach
def product_of_array_except_self(nums):
    """Returns an array which contains the pruduct of the original array exccluding the self."""
    for i in range(len(nums)):
        product = 1
        excluded_index = i
        for j in range(len(nums)):
            if j != excluded_index:
                product *= nums[j]
        answer.append(product)
    return answer


print(product_of_array_except_self(nums))

# Time Complexity is O(n^2) as there are two loops which run n times