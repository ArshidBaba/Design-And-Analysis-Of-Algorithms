"""
The Pascal's Traingle is inherently a Dynamic Programming Problem.
"""
output = []
numRows = 5
if numRows <= 2:
    if numRows < 2:
        output.append([1])
        # return
        print(output)
    else:
        output.append([1])
        output.append([1, 1])
        # return
        print(output)
else:
    output.append([1])
    output.append([1, 1])
    for i in range(2, numRows):
        temp = []
        # for j in range(0, i):
        j = 0
        while j <= i:
            if i == j or j == 0:
                temp.append(1)
            # elif i == j:
            #     temp.append(1)
            else:
                # print(i, j)
                temp.append(output[i - 1][j - 1] + output[i - 1][j])

            # print(i, j)
            j += 1
        output.append(temp)

    print(output)
