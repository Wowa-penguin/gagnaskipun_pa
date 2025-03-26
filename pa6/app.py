import time
from random import Random
from ui import Wordle
from file_man import FileMan
from error import WordIsNotRightSizeError, NotValidGameSizeError


class MainGame:
    def __init__(self):
        self.game = Wordle()
        self.word = []
        self.game_state = True

    def add_new_word(self, new_word):
        if len(new_word) != self.game.game_len:
            raise WordIsNotRightSizeError
        conn = FileMan(f"words/{self.game.game_len}letter.txt")
        conn.write_file(new_word)

    def select_random_word(self):
        ran = Random()
        conn = FileMan(f"words/{self.game.game_len}letter.txt")
        word_lis = conn.reed_file()
        selected_word = word_lis[ran.randint(0, len(word_lis) - 1)]
        while len(selected_word) == 0:
            selected_word = word_lis[ran.randint(0, len(word_lis) - 1)]
        for x in selected_word:
            self.word.append(x)
        print(self.word)

    def chack_word(self, word: list):
        count = 0
        curr_level = self.game.game_bord[f"Guess {self.game.curr_level}"]
        while count != self.game.game_len:
            if word[count] == self.word[count]:
                curr_level[count] = "C"
            elif word[count] in self.word:
                curr_level[count] = "c"
            count += 1

    def main_game_start(self):
        valid_start = True
        while valid_start:
            try:
                valid_start = self.game.start_game_upp()
            except NotValidGameSizeError:
                print(
                    f"{self.game.bold}{self.game.red}Not a valid game size bro\n Try again{self.game.end}"
                )
                time.sleep(3)

    def main_game_loob(self):
        self.main_game_start()
        self.select_random_word()
        self.game.display_game_bord()
        while self.game.curr_level < 6:
            print(self.word)
            try:
                user_word = self.game.paly_round()
            except WordIsNotRightSizeError:
                print(
                    f"{self.game.bold}{self.game.red}The word is of len {len(self.word)}{self.game.end}"
                )
                time.sleep(3)
                continue
            self.chack_word(user_word)
            if user_word == self.word:
                new_word = self.game.display_win(self.word)
                if new_word is not None:
                    try:
                        self.add_new_word(new_word)
                    except WordIsNotRightSizeError:
                        print(
                            f"{self.game.bold}{self.game.red}The word has to be same size aka {self.game.game_len} try one more time{self.game.end}"
                        )
                        try_again = input(
                            f"{self.game.blue}Enter the word of len {self.game.game_len}: {self.game.end}"
                        )
                        self.add_new_word(try_again)
                self.game.display_end(new_word)
                break
            self.game.curr_level += 1
            self.game.display_game_bord()


if __name__ == "__main__":
    t = MainGame()
    t.main_game_loob()
