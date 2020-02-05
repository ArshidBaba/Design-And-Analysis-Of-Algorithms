# This Python code is written from the pseudocode provided by the book 'Introduction to Algorithms
# by Cormen, Leiserson, Rivest, Stein. I have made a little changes here and there to suit it for Python.

def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

    return
def merge(A,p,q,r):
    MAX = 10000000000000000
    L = []
    R = []
    for i in range(p, q+1):
        L.append(A[i])
    for j in range(q+1, r+1):
        R.append(A[j])
    L.append(MAX)
    R.append(MAX)

    print(L)
    print(R)

    i = 0
    j = 0

    for k in range(p, r+1):
        if i < len(L) and j <len(R):
            if L[i] <= R[j]:
                A[k] = L[i]
                i += 1
            else:
                A[k] = R[j]
                j += 1
        elif i == len(L):
            A[k] = R[j]
        else:
            A[k] = L[i]
        print(A)
    
    return
    

if __name__ == "__main__":
    A = [2,4,5,7,1,2,3,6]
    # A = [8,7,6,5,4,3,2,1]
    p = 0
    q = (len(A)-1)//2
    r = len(A)-1

    print(A)
    print("p: ", p, "q: ", q, "r: ", r)

    merge_sort(A,p,r)