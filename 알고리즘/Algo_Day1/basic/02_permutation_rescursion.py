'''
배열을 순회해서, 요소를 선택하고, 순서를 바꾸서 출력
파이썬은 리스트를 변경하거나 크기를 늘이고 줄이는 행동이 자유롭다.

selected : 선택된 값 목록
remain: 선택되지 않은 값 목록
'''

def perm(selected, remain):
    '''
    재귀 함수 형식으로 코드를 작성
    -> basis part가 필요
    -> nPn 만큼 처리할 것이기 때문에, remain이 빈 경우
    '''
    if not remain: # 남은 값이 하나도 없다면? -> 모든 요소 사용
        print(selected)
    else: # 유도식 -> remain의 값을 하나씩 빼서 selected에 담는 것.
        for i in range(len(remain)):
            select_i = remain[i]
            # index 위치 번째 요소를 remain에서 제거하기 위해
            # remain.pop(i) -> 이걸 하진 않을 것.
                # 이유 : pop(i)의 연산 횟수는 O(N)이기 때문.
            # O(1) 연산을 수행할 것. -> 삭제된 요소 빼고 나머지를 새로운 리스트로 초기화.
            remain_list = remain[:i] + remain[i+1:]
            perm(selected + [select_i], remain_list)


# 이 함수를 호출한다면
perm([], [1,2,3])