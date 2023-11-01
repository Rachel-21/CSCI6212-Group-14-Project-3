"""
Code calculates the Longest common subsequence
between two strings.
"""
from random import choice
from statistics import mean
from string import ascii_uppercase
from textwrap import dedent
from time import perf_counter_ns
import os

import matplotlib.pyplot as plt


def generate_random_sequence(length) -> str:
    """
    Returns a random sequence of strings for
    computation of LCS.
    example sequence: 'LNIUNSWSBPDOZMBCLQBO'
    :return: String
    """
    return "".join(choice(ascii_uppercase) for _ in range(length))


class LongestCommonSubsequence:
    """
    Class to compute the LCS of given strings
    """
    def __init__(self, string_1, string_2):
        self.string_1 = string_1
        self.string_2 = string_2
        self.str_1_len = len(string_1)
        self.str_2_len = len(string_2)

    def get_common_character_indexes(self) -> list:
        """
        Returns the indexes of the common characters in two strings
        :return: dict
        """

        # create a zero list(list) of size m + 1
        # Used to calculate the index of the strings that match in the two strings
        common_char_index_list = [
            [0] * (self.str_2_len + 1) for _ in range(self.str_1_len + 1)
        ]

        # Update the corresponding list values + 1
        # if there is a match on the characters in both strings
        for i in range(1, self.str_1_len + 1):
            for j in range(1, self.str_2_len + 1):
                if self.string_1[i - 1] == self.string_2[j - 1]:
                    common_char_index_list[i][j] = (
                            common_char_index_list[i - 1][j - 1] + 1
                    )
                else:
                    common_char_index_list[i][j] = max(
                        common_char_index_list[i - 1][j],
                        common_char_index_list[i][j - 1],
                    )

        return common_char_index_list

    def longest_common_subsequence(self) -> list:
        """
        Calculates the longest common_subsequence between two strings
        :return: list
        """

        common_character_index_list = self.get_common_character_indexes()
        lcs = []
        i, j = self.str_1_len, self.str_2_len
        while i > 0 and j > 0:
            if self.string_1[i - 1] == self.string_2[j - 1]:
                lcs.append(self.string_1[i - 1])
                i -= 1
                j -= 1
            elif (
                    common_character_index_list[i - 1][j]
                    > common_character_index_list[i][j - 1]
            ):
                i -= 1
            else:
                j -= 1

        lcs = lcs[::-1]
        return lcs


if __name__ == "__main__":

    # String values lengths that we are running against
    test_values = [10, 100, 1000, 5000, 10000, 15000]
    experimental_times = []
    theoretical_times = []
    adjusted_theoretical_values = []
    curr_dir = os.getcwd()
    output_file_path = f"{curr_dir}/outputs.txt"

    # remove outputs file if it exists
    if os.path.exists(output_file_path):
        print("Output file already exists deleting file")
        os.remove(output_file_path)

    with open(output_file_path, "a") as f:
        # Run for each iteration of values to be tested
        for test_value in test_values:
            print(f"Running test_value {test_value}")
            random_gen_string_1 = generate_random_sequence(test_value)
            random_gen_string_2 = generate_random_sequence(test_value)

            start_time = perf_counter_ns()
            longest_common_subsequence = LongestCommonSubsequence(
                random_gen_string_1, random_gen_string_2
            ).longest_common_subsequence()
            end_time = perf_counter_ns()

            experimental_time_ns = end_time - start_time

            # Write output to file
            output_string = dedent(f"""\
                String 1 : {random_gen_string_1}
                String 2 : {random_gen_string_2}
                Longest Common Subsequence : {longest_common_subsequence}
                Time taken to perform subsequence on length {test_value} : {experimental_time_ns}
            \n
            """)
            f.write(output_string.lstrip())

            experimental_times.append(experimental_time_ns)

            theoretical_time = test_value * test_value  # n1*n2
            theoretical_times.append(theoretical_time)

    experimental_time_avg = mean(experimental_times)
    theoretical_time_avg = mean(theoretical_times)

    # Calculate scaling constant for adjusting theoretical value
    scaling_constant = experimental_time_avg / theoretical_time_avg

    for each_element in theoretical_times:
        adjusted_theoretical_values.append((each_element * scaling_constant))

    # Plot the data
    plt.plot(test_values, experimental_times, marker="o")
    plt.plot(test_values, adjusted_theoretical_values, marker="x", label="n^2")
    plt.title("Test Length vs. Elapsed Time")
    plt.xlabel("Test Length")
    plt.ylabel("Elapsed Time (ns)")
    plt.grid(True)
    plt.show()
