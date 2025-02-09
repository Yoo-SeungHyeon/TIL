import user
import post

class SNS:
    def __init__(self, users: list, posts: list):
        self.users = users
        self.posts = posts
    
    def add_user(self, username: str, email: str):
        user_obj = user.User(username, email)
        self.users.append(user_obj)
        return user_obj
    
    def add_post(self,user_obj: user.User, content:str):
        post_obj = post.Post(user_obj, content)
        self.posts.append(post_obj)
        return post_obj
    
    def get_post(self):
        return self.posts