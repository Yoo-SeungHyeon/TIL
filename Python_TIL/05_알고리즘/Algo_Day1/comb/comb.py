def comb(selected, remain, r):
    if not r:
        # print(selected)
        return [selected[:]]
    else:
        result = []
        for i in range(len(remain)-r+1):
            selected.append(remain[i])
            result.extend(comb(selected, remain[i+1:], r-1))
            selected.pop()
        return result

print(comb([], [1,2,3,4], 3))

# comb([], [1,2,3,4,5], 3)

def comb(arr, n):
    result = []
    if n == 1:
        return [[i] for i in arr]
    for i in range(len(arr)):
        elem = arr[i]
        for rest in comb(arr[i+1:], n-1):
            result.append([elem] + rest)
    return result

print(comb([1, 2, 3], 2))