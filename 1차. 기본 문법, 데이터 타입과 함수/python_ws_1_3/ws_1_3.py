users = [
    {"username": "alice", "age": 25, "is_active": True},
    {"username": "bob", "age": 17, "is_active": False},
    {"username": "charlie", "age": 30, "is_active": True},
    {"username": "david", "age": 22, "is_active": False},
    {"username": "eve", "age": 29, "is_active": True}
]

# 아래에 코드를 작성하시오.
import module as md

print("Adults:",md.age_over18_filter(users))
print("Active Users", md.active_True_filter(users))
print("Adults Active Users", md.age18_activeTrue_filter(users))