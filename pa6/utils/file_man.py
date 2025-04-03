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

    def reed_users(self) -> list[dict]:
        """Read the user info and returns the list of dicts"""
        with open(self.path, "r", encoding="utf-8") as conn:
            values = conn.read()
            temp_lis = values.split("\n")
            users = []
            for x in temp_lis:
                user = x.split(",")
                users.append(user)
            ret_lis = []
            for user in users:
                one_user = {
                    "name": user[0],
                    "win": int(user[1]),
                    "loss": int(user[2]),
                    "high_score": int(user[3]),
                }
                ret_lis.append(one_user)
            return ret_lis

    def sort_win(self, e):
        """To sort the list of dict"""
        return e["high_score"]

    def reed_top_five_users(self) -> list[dict]:
        """Get the top five users for the scoreboard at the start of the game"""
        users = self.reed_users()
        users.sort(key=self.sort_win, reverse=True)
        return users[0:5]

    def write_file(self, new_word: str) -> None:
        """write to a file in /words"""
        with open(self.path, "a", encoding="utf-8") as conn:
            conn.write(new_word + "\n")

    def add_user(self, new_user: str, wins: int, loss: int, high_score: int) -> None:
        """Add a user to the user files"""
        with open(self.path, "a", encoding="utf-8") as conn:
            user = f"{new_user},{wins},{loss},{high_score}"
            conn.write("\n" + user)

    def update_user_info(
        self, user_name: str, key: str, new_high_score: int = None
    ) -> None:
        """Update the user info by passing through the users and matching the username given
        Intex is given between 1 or 2
        1 is for win 2 is for loss"""
        users: list[dict] = self.reed_users()
        for user in users:
            if user_name == user["name"]:
                user[key] += 1
                if new_high_score:
                    user["high_score"] = new_high_score

        formatted_lis = []

        for x in users:
            value_str: str = ""
            for k, value in x.items():
                if k != "high_score":
                    value_str += str(value) + ","
                else:
                    value_str += str(value)
            formatted_lis.append(value_str)

        with open(self.path, "w", encoding="utf-8") as conn:
            for x in formatted_lis:
                if x == formatted_lis[-1]:
                    conn.write(x)
                else:
                    conn.write(x + "\n")


if __name__ == "__main__":
    pass
