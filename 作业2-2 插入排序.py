def insertionSort(arr): 
    for i in range(1, len): 
        key = arr[i]
        j = i-1
        while j >=0 and key <= arr[j] : 
                arr[j+1] = arr[j] 
                j -= 1
        arr[j+1] = key 
        for k in range(len-1): 
            print (arr[k],end=' ')
        print(arr[k+1])
len=int(input())
arr= input().split()
for i in range(len):
    arr[i]=int(arr[i])
insertionSort(arr)