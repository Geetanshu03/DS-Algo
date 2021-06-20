def binary_search_recursive(l,low,high,x):
    while(low <=high):
        mid = low + (high+low//2)
        if (l[mid] < x):
            return binary_search_recursive(l,mid+1,high,x)
        elif (l[mid] > x):
            return binary_search_recursive(l,low,mid-1,x)
        else:
            return mid
    
    return -1


if __name__ =='__main__':
    x=60
    l=[10,20,30,40,50,60,70]
    low=0
    high=len(l)-1
    print(binary_search_recursive(l,low,high,x))