'''
학생 점수 정보
   "Alice" = 85,
   "Bob" = 78,
   "Charlie" = 92,
   "David" = 88,
   "Eve" = 95
'''

# 아래에 코드를 작성하시오.
print("1. 학생들의 이름과 점수를 딕셔너리에 저장")
students = {"Alice": 85,"Bob": 78,"Charlie": 92,"David": 88,"Eve": 95}
print("students type:",type(students))
print("학생들의 이름과 점수:",students)
values = students.values()
values_len = len(values)
result2 = 0
for value in values:
   result2 += value
avg=result2/values_len
print(f"2. 모든 학생의 평균 점수: {avg:.2f}")
result3 = []
for key in students.keys():
   if students.get(key) >= 80:
      result3.append(key)
print("3. 기준 점수(80점) 이상을 받은 학생 수:",result3)
print("4. 점수 순으로 정렬:")
for key,value in sorted(students.items(), key=lambda x:x[1], reverse=True):
   print(f"{key}: {value}")
max = sorted(students.values(), reverse=True)[0]
min = sorted(students.values())[0]
print(f"5. 점수가 가장 높은 학생과 가장 낮은 학생의 점수 차이: {max-min}")
print("6. 각 학생의 점수가 평균보다 높은지 낮은지 판단:")
for key,value in students.items():
   if value > avg:
      updown = "이상"
   else:
      updown = "이하"
   print(f"{key} 학생의 점수({value})는 평균 {updown}입니다.")