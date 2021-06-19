def binary_search(l,x):
    n=len(l)
    low=0
    high=n-1
    mid=0
    while(low <= high):
        # mid is calculated this way to avoid overflow error
        mid = low + (high+low//2)
        if (l[mid] < x):
            low = mid+1
        elif (l[mid] > x):
            high = mid -1
        else:
            return mid
    return -1
if __name__ == '__main__':
    x=60
    l=[10,20,30,40,50,60,70]
    print(binary_search(l,x))



