# insertion_sort method
def insertion_sort(lst2):
    ''' insertion_sort method implements insertion sort algorithm and sorts the input array.'''
    for j in range(1,len(lst2)):
        key = lst2[j]
        i = j - 1
        while i >= 0 and lst2[i] > key:
            lst2[i+1] = lst2[i]
            i = i - 1
        lst2[i+1] = key
    return lst2

# main method
def main():
    ''' main method takes input from console and calls insertion_sort method.'''
    msg = "Enter the array: "
    print(msg)
    lst1 = []
    lst1 = [int(item) for item in input("Enter the list items : ").split()]
    # print(lst1)
    print("The sorted array is: ", insertion_sort(lst1))


if __name__ == "__main__":
    main()