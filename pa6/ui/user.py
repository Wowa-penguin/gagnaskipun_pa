from utils.file_man import FileMan
from error import NoUserFund


class User:
    """A user class to hold the username and win loss stats"""

    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loss = 0
        self.score = 0

    def get_palyer_info(self):
        conn = FileMan("user/users.tex")
        users_lis = conn.reed_users()
        for user in users_lis:
            if self.name == user[0]:
                return user
        raise NoUserFund

    def add_user(self) -> None:
        conn = FileMan("user/users.tex")
        conn.add_user(self.name, self.wins, self.loss)


if __name__ == "__main__":
    pass
    # user = User("Heimir")
    # print(user.get_palyer_info())
