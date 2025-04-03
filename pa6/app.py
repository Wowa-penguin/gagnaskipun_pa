import time
from random import Random
from ui import Wordle, User
from utils.file_man import FileMan
from error import WordIsNotRightSizeError, NotValidGameSizeError, NoUserFund


class MainGame:
    """Main game class to handle the logic"""

    def __init__(self):
        self.game = Wordle()
        self.word = []
        self.user: User = None

    def add_new_word(self, new_word) -> None:
        """Add a new word To the word bank by creating a connection with File Manager class"""
        if len(new_word) != self.game.game_len:
            raise WordIsNotRightSizeError
        conn = FileMan(f"words/{self.game.game_len}letter.txt")
        conn.write_file(new_word)  # Write the word to the file

    def select_random_word(self) -> None:
        """Select a random word from the word bank"""
        ran = Random()
        conn = FileMan(f"words/{self.game.game_len}letter.txt")
        word_lis = conn.reed_file()
        selected_word = word_lis[ran.randint(0, len(word_lis) - 1)]
        while len(selected_word) == 0:
            selected_word = word_lis[ran.randint(0, len(word_lis) - 1)]
        for x in selected_word:
            self.word.append(x)
        print(self.word)

    def chack_word(self, word: list) -> None:
        """Check the guess word with the correct word.
        Add the corresponding uppercase C or lowercase c to display to the user"""
        count = 0
        curr_level = self.game.game_bord[f"Guess {self.game.curr_level}"]
        while count != self.game.game_len:
            if word[count] == self.word[count]:
                curr_level[count] = "C"
            elif word[count] in self.word:
                curr_level[count] = "c"
            count += 1

    def select_user(self) -> None:
        """Select the user from the input and checks if the user exists, if not create a user"""
        conn = FileMan("user/users.tex")
        user_name = self.game.selcet_user_at_start(conn.reed_top_five_users())
        try:
            self.user = User(user_name)
            self.user.get_palyer_info()
        except NoUserFund:
            self.user.add_user()

    def start_valid_game(self):
        """Makes sure that the game size and guess size are valid by checking if an NotValidGameSizeError is raised"""
        valid_game = True
        while valid_game:
            try:  # Try Expect for starting up the game with valid settings
                valid_game = self.game.start_game_upp(self.user)
            except NotValidGameSizeError:
                print(
                    f"{self.game.bold}{self.game.red}Not a valid game size bro\n Try again{self.game.end}"
                )
                time.sleep(3)

    def main_game_loob(self, is_replay: bool) -> None:
        """The main game loop function which manages the game from start to finish"""
        game_won = False
        if not is_replay:
            self.select_user()
        self.start_valid_game()
        self.select_random_word()
        self.game.display_game_bord()
        while self.game.curr_level < self.game.guesses + 1:
            print(self.word)  #! Delete this

            try:  # Try except for getting valid user input
                user_word = self.game.paly_round()
            except WordIsNotRightSizeError:
                self.game.clear()
                print(
                    f"{self.game.bold}{self.game.red}The word is of length {len(self.word)}{self.game.end}"
                )
                print(
                    f"{self.game.bold}{self.game.red}Your guess has to be of the sem length{self.game.end}"
                )
                time.sleep(4)  # Gives the user time to read the message
                self.game.clear()
                self.game.display_game_bord()
                continue  # back to the top loop

            self.chack_word(user_word)
            if user_word == self.word:
                game_won = True
                # Checks if the user wants to add a new word and replay the game
                new_word = self.get_new_word()
                replay = self.game.display_end(new_word)
                break  # Breaks the main wide loop
            self.game.curr_level += 1
            self.game.display_game_bord()
        # Check if the game is won
        if not game_won:  # Game lost
            replay = self.game.display_loss("".join(self.word))
            self.user.loss += 1
            self.uppdate_user_info("l")
        else:  # Game won
            self.user.wins += 1
            self.uppdate_user_info("w")
        # Check if a replay is true
        if replay:
            self.replay_game()
            return True
        return False

    def uppdate_user_info(self, status: str) -> None:
        """Update the user win and loss ratio
        Create a connection to the user text file which returns the user data in a list
        The list is formatted from the File Manager class so
        win in the first index and loss in a second index
        """
        try:
            conn = FileMan("user/users.tex")
            user_info = self.user.get_palyer_info()
            user_info[1] = self.user.wins
            user_info[2] = self.user.loss
            if status == "w":
                conn.update_user_info(self.user.name, "win")
            elif status == "l":
                conn.update_user_info(self.user.name, "loss")
        except NoUserFund:  # If user doesn't exist add them to the database base
            self.user.add_user()

    def replay_game(self) -> None:
        """After a game has been played and the player wants to play again,
        this function resets the game"""
        new_game = Wordle()
        self.game = new_game
        self.word = []

    def get_new_word(self) -> str | None:
        """Gets a new word from the user to add to the word bank"""
        new_word = self.game.display_win(self.word)  # -> str or None
        if new_word is not None:
            while new_word is not None:
                try:
                    self.add_new_word(new_word)
                    break  # success on adding the word
                except WordIsNotRightSizeError:
                    print(
                        f"{self.game.bold}{self.game.red}The word has to be the same size ({self.game.game_len}). Try again.{self.game.end}"
                    )
                    new_word = input(
                        f"{self.game.blue}Enter a word of length {self.game.game_len}: {self.game.end}"
                    )
        return new_word


def main():
    """Main"""
    game_live = True
    replay_on = False
    game = MainGame()
    while game_live:
        game_live = game.main_game_loob(replay_on)
        replay_on = True


if __name__ == "__main__":
    main()
