def counting (arr, k):
    ## đếm số lượng từng phần tử trong mảng arr, với số lớn nhất là k
    count = [0] * k
    for i in arr:
        count [i] += 1
    return count

def counting_sort (arr):
    k = max(arr) + 1
    counts = counting (arr, k)
    result = []
    for i in range(k):
        result.extend([i]*counts[i])
    return result

arr = [5,3,6,2,6,4,3,4,2,4,1,4,5,3,6,3,2,1,3]
print(counting_sort(arr))
