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
                print(A)
                print(i, j)
                count += 1
    print(A)
    print(count)
    return

if __name__ == "__main__":
    A = [2, 4, 1, 3, 5]
    inverse(A)
