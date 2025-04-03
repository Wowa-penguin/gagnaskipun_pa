from os import name, system
from error import WordIsNotRightSizeError, NotValidGameSizeError


class UiMain:
    """Main ui class to add color to the terminal window"""

    def __init__(self) -> None:
        self.black = "\033[0;30m"
        self.red = "\033[0;31m"
        self.green = "\033[0;32m"
        self.brown = "\033[0;33m"
        self.blue = "\033[0;34m"
        self.purple = "\033[0;35m"
        self.cyan = "\033[0;36m"
        self.light_gray = "\033[0;37m"
        self.dark_gray = "\033[1;30m"
        self.light_red = "\033[1;31m"
        self.light_green = "\033[1;32m"
        self.yellow = "\033[1;33m"
        self.light_blue = "\033[1;34m"
        self.light_purple = "\033[1;35m"
        self.light_cyan = "\033[1;36m"
        self.light_white = "\033[1;37m"
        self.orange = "\033[38;5;214m"
        self.bold = "\033[1m"
        self.faint = "\033[2m"
        self.italic = "\033[3m"
        self.underline = "\033[4m"
        self.blink = "\033[5m"
        self.negative = "\033[7m"
        self.crossed = "\033[9m"
        self.end = "\033[0m"

    def clear(self) -> None:
        """To clear the terminal window"""
        if name == "nt":
            system("cls")
        else:
            system("clear")


class Wordle(UiMain):
    """The ui wordle game class to display the game bord and level"""

    def __init__(self):
        self.game_bord = {}
        self.user_name = ""
        self.game_len = 0
        self.guesses = 0
        self.curr_level = 1
        super().__init__()

    def selcet_user_at_start(self, users: list[dict]) -> None:
        """Displaced the score table with the top five users and lets the user select a username"""
        self.clear()
        print(f"{self.blue}{self.bold}Here is wordle{self.end} \n")
        self.display_score_table(users)
        self.user_name = input(
            f"{self.bold}Plis enter a username for your self: {self.end}"
        )
        return False  # To break the loop in app.py

    def start_game_upp(self) -> None:
        """The start up display function, let's the user set the game length and guesses values"""
        self.clear()
        # Ask the user for how many letters are in the word
        print(f"{self.red}{self.bold}From 3 to 10{self.end}")
        self.game_len = int(
            input(f"{self.bold}Enter how meny lettars you want in the word: {self.end}")
        )
        if not 2 < self.game_len < 11:
            self.clear()
            raise NotValidGameSizeError

        # Ask the user how many guesses they want
        print(f"{self.red}{self.bold}From 1 to 10{self.end}")
        self.guesses = int(
            input(f"{self.bold}Enter how meny guesses do you want: {self.end}")
        )
        if not 1 < self.guesses < 11:
            self.clear()
            raise NotValidGameSizeError

        # Create the game board dict
        self.make_bord(self.guesses)
        for value in self.game_bord.values():
            value *= self.game_len
        self.clear()

    def make_bord(self, length: int) -> None:
        """Create the game board with level and guesses in a dictionary"""
        for x in range(length):
            self.game_bord[f"Level {x+1}"] = ["?"]
            self.game_bord[f"Guess {x+1}"] = ["-"]

    def display_game_bord(self) -> None:
        """To display the game bord to the window"""
        self.clear()
        print(f"{self.cyan}User: {self.user_name}{self.end}\n")
        for key, value in self.game_bord.items():
            # The keys in the bord are str thet start with Level or guess followed by the a number from 1 to 5
            level_to_stop = key.split(" ")
            if int(level_to_stop[-1]) > self.curr_level:
                # To only display the level the game is at and help with time complexity max is O(N X M)
                break
            level = f"Level {self.curr_level}"
            if key == level:  # if key is level
                print(f"{self.green}{self.bold}{key}{self.end}", end=" ")
            else:  # if key is Guess
                print(f"{self.light_gray}{key}{self.end}", end=" ")
            if "Guess" in key:  # Chack if the "Guess" is in the key
                for x in value:
                    print(self.format_guess_char(x), end=" ")
            else:
                print(f"| {" | | ".join(value)} |", end=" ")
            print("\n")

    def format_guess_char(self, x):
        """To format the colors in the bord for guesses"""
        color = {
            "-": self.red,
            "C": self.green,
            "c": self.yellow,
        }.get(x, self.end)
        return f"|{color} {x} {self.end}|"

    def display_score_table(self, users: list[list]) -> None:
        """Display the top five users with the highest win score"""
        print(f"{self.cyan}Top five users!{self.end}")
        print(f"{self.bold}{'Name':<15}{'Wins':<10}{'Losses':<10}{self.end}")
        print("-" * 35)
        for user in users:
            print(f"{user["name"]:<15}{user["win"]:<10}{user["loss"]:<10}")
        print("")  # add a space at the end

    def paly_round(self) -> None:
        """Gets the user input for a word guess and plays one round"""
        print(self.curr_level)
        user_input = input(f"Enter a {self.game_len} letter word: ").replace(" ", "")
        user_word_lis = []
        for x in user_input:
            user_word_lis.append(x)
        if len(user_word_lis) != self.game_len:  # if the guess word is not the sem size
            raise WordIsNotRightSizeError
        self.game_bord[f"Level {self.curr_level}"] = user_word_lis
        return user_word_lis  # return the guess

    def display_win(self, corect_word: list) -> str | None:
        """Function to diplay the win window to the user
        it also asks for a new word returns None if no new word"""
        self.clear()
        print(
            f"{self.cyan}{self.user_name} You win the word was ({"".join(corect_word)}){self.end}"
        )
        make_new_word = input(
            f"{self.yellow}Do you want to add a new word if not type (q): {self.end}"
        )
        self.clear()
        if make_new_word.lower() != "q":
            return make_new_word
        return None

    def display_loss(self, word) -> None:
        """Function to diplay the loss window"""
        self.clear()
        print(
            f"{self.purple}Ty for playing better luck next time the word was {self.bold}{self.blue}{word}{self.end}"
        )
        ask_for_new_game = input(
            f"{self.light_green}Do you want to play again? (yes q for no) \n: {self.end}"
        )
        if ask_for_new_game.lower() == "q":  # if user doesn't want to play again
            self.clear()
            print(f"{self.green}Have a good day :){self.end}")
            return None
        return ask_for_new_game  # just returns str ass if it doesn't return None then it plays again

    def display_end(self, new_word: str | None) -> str | None:
        """Function to diplay the end window to the user
        it gets the new word if it exists otherwise it gets None
        returns str if user wants to play again"""
        self.clear()
        if new_word:  # if a new word
            print(
                f"{self.purple}Ty for playing and for the new word of {self.bold}{self.blue}{new_word}{self.end}"
            )
        else:  # if no new word
            print(f"{self.purple}Ty for playing{self.end}")
        ask_for_new_game = input(
            f"{self.light_green}Do you want to play again? (yes q for no) \n: {self.end}"
        )
        if ask_for_new_game.lower() == "q":  # if user doesn't want to play again
            self.clear()
            print(f"{self.green}Have a good day :){self.end}")
            return None
        return ask_for_new_game  # just returns str ass if it doesn't return None then it plays again
