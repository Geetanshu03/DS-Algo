
'''
1 3 5 6 7 9

'''

def search_in_sorted_arr(arr,x):
    low=0
    high = len(arr)
    while (low <= high):
        mid = low + (high-low)//2
        if (arr[mid] ==x):
            return mid
        if (arr[low] < arr[mid]): #means  for the first time left half array is sorted
            if (arr[low] <= x and arr[mid] > x):
                high = mid -1
            else:
                low = mid +1
        else:
            if (arr[mid] < x and arr[high]>= x):
                low = mid +1
            else:
                high= mid -1
    
    return -1
        
            

if __name__ =='__main__':
    arr=[10,20,30,40,50,8,9]
    x=30
    print(search_in_sorted_arr(arr,x))

