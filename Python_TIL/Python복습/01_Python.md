# Python
Pypy 덕분에 python은 더이상 느린 언어가 아니다.

# Data Type 
> -> 값의 속성과 종류를 정의하는 것

> 그러면 자료구조는 뭘까? 
> -> 효율적으로 저장, 조직화 관리하는 것을 의미함.

1. Numeric Type
2. Text Sequence Type
3. Sequence Types
4. Non-sequence Types
5. 기타

## 타입과 메서드

**Method**

객체에 속한 함수.

동작 자체는 함수와 동일하지만 객체에 속해있다는 사실이 다르다.

객체 지향에만 존재한다.

-> Python의 각종 데이터 타입에는 그에 적합한 메서드가 존재한다

## Numeric Type

- [x] **int** : 정수

- [x] **float** : 실수

- [x] **complex** : 존재 정도만 알아두자

- [x] 지수 표현 방식도 제공한다. (e나 E를 사용하는 표현 방식)

## Sequence Types : 여러 값을 순서대로 나열하여 저장하는 자료형

**특징**
1. 순서 (주의!! 정렬을 의미하는 것이 아님)
2. 인덱싱
3. 슬라이싱
4. 길이
5. 반복

### **str**
- 변경 불가능한 시퀀스 자료형
- f-string으로 문자열 내부에 변수의 값을 입력할 수 있음
- python 3.6 이상부터 f-string 사용 가능
- 슬라이싱 with step
    ```python
    my_str = "hello"
    my_str[0:5:2] # 0에서 5까지 2칸씩
    ```
- 문자열 조작 메서드
    1. replace
    2. strip
    3. split
    4. join : 문자열의 메서드이다. 헷갈리지 말자.

### **list**
- 변경 가능한 시퀀스 자료형
- 가변형 자료형
- 어떤 자료형도 저장 가능
- \[\] 로 표현함
- 리스트 메서드
    ```python
    append
    extend
    pop : '인덱스'를 인자로 받기도 한다.
    reverse
    sort
    ```