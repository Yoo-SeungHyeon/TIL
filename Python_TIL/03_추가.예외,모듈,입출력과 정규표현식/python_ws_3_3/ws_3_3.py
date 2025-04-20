# 3444. SNS 시스템 만들기 3 Lv3
# 아래에 코드를 작성하시오.
'''
요구사항
user.py 파일을 작성하여 사용자(User) 클래스를 정의하세요.
post.py 파일을 작성하여 게시물(Post) 클래스를 정의하세요.
sns.py 파일을 작성하여 사용자와 게시물을 관리하는 SNS 클래스를 정의하세요.
SNS 클래스는 users와 posts 두 개의 리스트 인스턴스 변수를 가져야 합니다.
add_user 메서드는 사용자명을 나타내는 username과 이메일을 나타내는 
email을 인수로 받아 새로운 User 객체를 생성하고 users 리스트에 추가합니다. 
생성된 User 객체를 반환합니다.
add_post 메서드는 user 객체와 content를 인수로 받아 새로운 Post 객체를 
생성하고 posts 리스트에 추가합니다. 생성된 Post 객체를 반환합니다.
get_posts 메서드는 모든 게시물 객체를 반환합니다.
sns 모듈을 import 하여 사용자 생성, 게시물 작성 및 조회 기능의 
정상 동작을 확인하세요.
'''

import sns

sns = sns.SNS([],[])

john =sns.add_user('john_doe', 'john_doe@example.com')
sns.add_post(john, 'Hello, this is my first post!')
sns.add_post(john, 'Hi everyone, glad to be here!')

for post in sns.get_post():
    print(post)
