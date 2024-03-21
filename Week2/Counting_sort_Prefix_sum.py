def counting (arr, k):
    ## đếm số lượng từng phần tử trong mảng arr, với số lớn nhất là k
    count = [0] * k
    for i in arr:
        count [i] += 1
    return count

def prefix_sum(arr):
    for i in range(1,len(arr)):
        arr[i] += arr[i-1]
    return arr

def counting_sort (arr):
    k = max(arr) + 1
    counts = counting (arr, k)
    counts = prefix_sum(counts)
    result = [0]*len(arr)
    while (counts[k-1] != 0):
        for i in range (counts[k-1]):
            result [i] = k-1
        k -= 1
    return result

arr = [5,3,6,2,6,4,3,4,2,4,1,4,5,3,6,3,2,1,3]
print(counting_sort(arr))