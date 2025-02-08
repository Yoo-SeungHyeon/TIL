# 04_backtracking

def find_subset(start, current_subset, current_sum):
    # print(current_subset, current_sum)
    if len(current_subset) == R:
        if current_sum == target_num:
            result.append(current_subset[:])
        return

    # 가지치기 추가
    if current_sum > target_num:
        return
    # print(current_subset, current_sum)
    # 일단 완전 탐색을 해
    # 현재 선택한 대상 idx 부터 마지막 요소까지
    for i in range(start, len(numbers)):
        selecte_num = numbers[i]
        # 현재 수를 선택 -> 현재 부분집합에 해당 요소를 삽입.
        current_subset.append(selecte_num)
        # 선택한 요소와 함께 다음 요소를 선택하러 떠난다.
        find_subset(i + 1, current_subset, current_sum + selecte_num)  # 단, 현재 요소 다음 요소부터 선택하도록 한다.
        current_subset.pop()


numbers = list(range(1, 11))
target_num = 19 # 5개의 합이 19인 경우
print(numbers)
R = 5
result = []
# DFS로 진행할 때 필요한 파라미터
# 1. 재귀를 중단 시킬 파라미터 -> 5개를 모두 선택했다면 종료 (모든 선택지를 볼 필요 없음.)
# 2. 누적해서 가져가야 할 값들. -> 부분집합을 만드는 것이 목적
# 현재 선택할 원소를 가리키는 idx
find_subset(start=0, current_subset=[], current_sum=0)
print(result)
