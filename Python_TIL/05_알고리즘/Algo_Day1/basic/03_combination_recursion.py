# arr 배열에서 r개의 요소를 선택해서 조합을 생성
def comb(arr, r):
    result = [] # 최종 결과물
    # basis part
    # r -> 1까지
    # r이 1이면 더이상 조합할 요소가 없음
    if r == 1:
        return [[i] for i in arr]
    # 유도식
    for i in range(len(arr)):
        select_i = arr[i] # 현재 요소 선택
        # 현재 요소 이후의 나머지 요소들로 r-1개의 조합을 생성
        for rest in comb(arr[i+1:], r - 1):
            # 현재 선택한 요소 + 재귀 호출 해서 얻은 조합 합침
            result.append([select_i] + rest)
    return result

# nCr
# n => 4
# r => 3
print(comb([1,2,3,4], 3))