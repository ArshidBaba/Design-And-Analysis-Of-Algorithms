l = [13, 11, 9, 7, 6, 4, 2, 1]

i = 0
size = len(l)
while size > 0:
    i = 0
    j = i + 1
    while j < size:
        if l[i] > l[j]:
            temp = l[i]
            l[i] = l[j]
            l[j] = temp
        j += 1
        i += 1
        print("Temp Array: ", l)
    size -= 1


print("The Sorted Array: ", l)
