from user import User


class Post:
    def __init__(self, header: str, body: str, author: User):
        self.body = body
        self.author = author
