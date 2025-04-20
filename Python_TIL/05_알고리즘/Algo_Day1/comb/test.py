arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
result = []

arr1.extend(arr2)

result.extend(arr1)

print(result)