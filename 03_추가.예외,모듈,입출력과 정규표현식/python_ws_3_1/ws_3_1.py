# 아래에 코드를 작성하시오.
'''
3442. SNS 시스템 만들기 1 Lv1
요구사항
user.py라는 사용자 정의 모듈을 작성한다.
user.py 모듈에는 User 클래스를 정의한다.
User 클래스는 사용자의 이름과 이메일을 속성으로 가진다.
User 클래스는 사용자의 정보를 출력하는 display_info 메서드를 가진다.
main.py 파일을 작성하여 user.py 모듈을 import 한다.
main.py에서 User 클래스를 사용하여 두 명의 사용자를 생성하고, 각 사용자의 정보를 출력한다.
'''

import user

a = user.User('Alice', 'alice@example.com')
b = user.User('Bob', 'bob@example.com')

a.display_info()
b.display_info()