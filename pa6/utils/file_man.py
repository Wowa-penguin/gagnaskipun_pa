class FileMan:
    """A general file management class for opening and reading files"""

    def __init__(self, path: str):
        self.path = path

    def reed_file(self) -> list:
        """Read a file in /words"""
        ret_lis = []
        with open(self.path, "r", encoding="utf-8") as conn:
            word = conn.read()
            word_list = word.split("\n")
        for w in word_list:
            new_word = w.strip()
            ret_lis.append(new_word)
        return ret_lis

    def reed_users(self) -> list[list]:
        """Read the user info and returns the list"""
        with open(self.path, "r", encoding="utf-8") as conn:
            users = conn.read()
            users_lis = users.split("\n")
            ret_lis = []
            for x in users_lis:
                user = x.split(",")
                ret_lis.append(user)
            return ret_lis

    def write_file(self, new_word: str) -> None:
        """write to a file in /words"""
        with open(self.path, "a", encoding="utf-8") as conn:
            conn.write(new_word + "\n")

    def add_user(self, new_user: str, wins: int, loss: int) -> None:
        """Add a user to the user files"""
        with open(self.path, "a", encoding="utf-8") as conn:
            user = f"{new_user},{wins},{loss}"
            conn.write("\n" + user)

    def update_win(self, user_name) -> None:
        """Update the win for a user"""
        users_lis = self.reed_users()
        for user in users_lis:
            if user_name in user:
                user[1] = int(user[1]) + 1
                user[1] = str(user[1])
                break
        with open(self.path, "w", encoding="utf-8") as conn:
            for x in users_lis:
                if x == users_lis[-1]:
                    conn.write(",".join(x))
                else:
                    conn.write(",".join(x) + "\n")

    def update_loss(self, user_name) -> None:
        """Update the loss for a user"""
        users_lis = self.reed_users()
        for user in users_lis:
            if user_name in user:
                user[2] = int(user[2]) + 1
                user[2] = str(user[2])
                break
        with open(self.path, "w", encoding="utf-8") as conn:
            for x in users_lis:
                if x == users_lis[-1]:
                    conn.write(",".join(x))
                else:
                    conn.write(",".join(x) + "\n")

    def update_user_info(self, user_name: str, index: int) -> None:
        """Update the user info by passing through the users and matching the username given
        Intex is given between 1 or 2
        1 is for win 2 is for loss"""
        users_lis = self.reed_users()
        for user in users_lis:
            if user_name in user:
                user[index] = int(user[index]) + 1
                user[index] = str(user[index])
                break
        with open(self.path, "w", encoding="utf-8") as conn:
            for x in users_lis:
                if x == users_lis[-1]:
                    conn.write(",".join(x))
                else:
                    conn.write(",".join(x) + "\n")


if __name__ == "__main__":
    pass
