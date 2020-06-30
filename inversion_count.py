def swap(a, b):
    temp = a
    a = b
    b = temp
    return (a, b)
def inverse(A):
    count = 0
    temp = 0
    for i in range(len(A)-1):
        for j in range(i+1, len(A)):
            if A[i] > A[j]:
                A[i], A[j] = swap(A[i], A[j])
                # print(A)
                # print(i, j)
                count += 1
    # print(A)
    # print(count)
    # print(tuple(i,j))
    return count

if __name__ == "__main__":
    # A = [2, 4, 1, 3, 5]
    count = 0
    print(count)
    with open("IntegerArray.txt") as f:
        A = [int(line.rstrip('\n')) for line in f]
    count = inverse(A)
    print("\n",count,"\n")
