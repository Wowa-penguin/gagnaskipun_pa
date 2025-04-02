class FileMan:
    def __init__(self, path: str):
        self.path = path

    def reed_file(self) -> list:
        ret_lis = []
        with open(self.path, "r", encoding="utf-8") as conn:
            word = conn.read()
            word_list = word.split("\n")
        for w in word_list:
            new_word = w.strip()
            ret_lis.append(new_word)
        return ret_lis

    def reed_users(self) -> list[list]:
        with open(self.path, "r", encoding="utf-8") as conn:
            users = conn.read()
            users_lis = users.split("\n")
            ret_lis = []
            for x in users_lis:
                user = x.split(",")
                ret_lis.append(user)
            return ret_lis

    def write_file(self, new_word: str) -> None:
        with open(self.path, "a", encoding="utf-8") as conn:
            conn.write(new_word + "\n")

    def add_user(self, new_user: str, wins: int, loss: int) -> None:
        with open(self.path, "a", encoding="utf-8") as conn:
            user = f"{new_user},{wins},{loss}"
            conn.write("\n" + user)

    def uppdate_win(self, user_name) -> None:
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

    def uppdate_loss(self, user_name) -> None:
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


if __name__ == "__main__":
    pass
