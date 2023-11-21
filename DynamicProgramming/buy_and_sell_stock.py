prices = [7, 1, 5, 3, 6, 4]
# prices = [7, 6, 4, 3, 1]
# prices = [1, 2]

"""
1st approach is a brute force approach, while the 2nd approach is a dynamic programming solution
"""
# diff = 0
# i = len(prices) - 1
# print(i)
# for i in reversed(range(0, len(prices) - 1)):
#     print("outter loop")
#     print("i: ", i)
#     for j in reversed(range(0, i)):
# while i > 0:
#     j = i - 1
#     while j >= 0:
#         if prices[i] - prices[j] < 0:
#             break
#         if prices[i] - prices[j] > diff:
#             # print(diff)
#             diff = prices[i] - prices[j]
#             # print(diff)
#         j -= 1

#     i -= 1

# print(diff)

maxProfit = 0
mini = prices[0]
i = 1
while i < len(prices):
    curProfit = prices[i] - mini
    maxProfit = max(maxProfit, curProfit)
    mini = min(mini, prices[i])
    i += 1

print(maxProfit)
