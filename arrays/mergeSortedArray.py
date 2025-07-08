nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3


# nums1 = nums1[0:m]

for i in range(m, len(nums1)):
    nums1.pop(m)

for i in range(n):
    nums1.append(nums2[i])

nums1.sort()

print(nums1)
