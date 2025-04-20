import user

class Post:
    def __init__(self, user_obj: user.User, content: str):
        self.user_obj = user_obj
        self.content = content

    def __str__(self):
        return f'Post(user={self.user_obj.username}, content={self.content})'