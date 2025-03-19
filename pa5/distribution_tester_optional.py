import hashlib
import matplotlib.pyplot as plt
import random
import numpy as np
from scipy import stats

"""
IMPORTANT! READ FIRST!
This script takes your hashfunction and tests it and plots the results to visualize how your hash performs.
This is not required and no extra points are given for using this.
You need to install three python packages, but before you do that it's recommended to create a virtual environment.
To create virtual environment execute `python3 -m venv env` in the terminal in your workspace. 
Then you have to source it with the command `source env/bin/activate`.
Now you are in a virtual environment and can install the packages with out them installing globally.
In the terminal run `pip3 install matplotlib numpy scipy` and now you should be able to run the code, given it's in the same workspace.

Note: remember to close the plot window for next run.
"""


m = hashlib.sha256()
length_of_list = 1000
amount_of_hashes = 1000000


def distribution_value(my_list):
    std = np.std(my_list)
    zscore = stats.zscore(my_list, axis=None)
    print(f"standard deviation: {std}")
    print(f"Z score is: {zscore}")
    print(f"Average zscore: {np.mean(zscore)}")


def plotter(my_list):
    plt.plot(my_list)
    plt.ylim(bottom=0)
    plt.show()


def hakon_hasher():
    random_word = b""
    for _ in range(10):
        random_word += chr(random.randint(65, 122)).encode("ascii")
    hashed_string = hashlib.sha256(random_word).hexdigest()
    hashed_number = int(hashed_string, base=16)
    return hashed_number


def distribution():
    my_list = [0 for _ in range(length_of_list)]
    for i in range(amount_of_hashes):
        # you can import your function and replace this function call.
        hashed_number = hakon_hasher()
        my_list[hashed_number % length_of_list] += 1
    return my_list


if __name__ == "__main__":
    my_list = distribution()
    # print(my_list)
    distribution_value(my_list)
    plotter(my_list)
