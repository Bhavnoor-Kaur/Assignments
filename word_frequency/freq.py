# --------------------------------------------
# Name: Bhavnoor Kaur
# ID: 1623727
# CMPUT 274, Fall 2020
#
# Weekly Exercise 3: Word Frequency
# --------------------------------------------

import sys
import collections


def extract_file():
    """
    This function opens the input file provided by the user and
    extracts the information splitting the lines and storing them
    into a list.

    Arguments:
               None

    Return:
           filename: the name of the inputfile
    """

    global line_list
    global filename

    # Checks for the absence of the input file name and prints out an error
    # message along with the proper usage of the program
    if len(sys.argv) == 1:
        print("There are too few command line arguments.")
        print("The proper usage is:")
        print("python3 freq.py <input_file_name>")
        print("where <input_file_name> is the name of the input file.")
        sys.exit()

    # Checks for presence of too many command line arguments and prints
    # out an error message along with the proper usage of the program.
    elif len(sys.argv) > 2:
        print("There are too many command line arguments.")
        print("The proper usage is:")
        print("python3 freq.py <input_file_name>")
        print("where <input_file_name> is the name of the input file.")
        sys.exit()

    # Extracting a list which contains a all the lines from the inout file
    # as the elemnts
    elif len(sys.argv) == 2:

        filename = sys.argv[1]
        input_file = open(filename, 'r')
        line_list = input_file.read().splitlines()
        input_file.close()
        return filename


def word_counter():
    """
    This function stores the words from individual lines and sorts
    them according to lexicographic order, stores them in a list
    Counts the number of times each word appears and stores them in a list
    Calculates the frequency of every word - which is the ratio of
    the count of the word to the total number of words.

    Arguments:
              None

    Return:
            table - a list consisting of elements that stores the word,
            count, frequency
    """
    # Creating global variables
    global word_list
    global word_count
    global sorted_words
    global sorted_count
    global sorted_freq
    global table

    # Creating empty lists for the variables
    word_list = []
    sorted_count = []
    sorted_freq = []
    table = []

    # Creating a list of words by splitting the lines
    for line in line_list:
        word = line.split()
        word_list.extend(word)

    # Counting the number of times each word appears in the list
    # and storing the word and count into a dictionary
    word_count = collections.Counter(word_list)

    # Sorting in the keys of the dictionary in Lexicographic order
    # and storing them in a list
    sorted_words = sorted(word_count.keys())

    # Storing the count of the words in a list
    for s_word in sorted_words:
        sorted_count.append(word_count[s_word])

    # Count the total number of words present in the file
    total_count = sum(word_count.values())

    # Calculating and storing the frequency of the words
    # in a list
    for s_count in sorted_count:
        sorted_freq.append(round((s_count/total_count), 3))

    # Creating a list contining the word, the count and the frequency
    for i in range(len(sorted_words)):
        row = str(sorted_words[i]) + " " + str(sorted_count[i])
        row = row + " " + str(sorted_freq[i])
        table.append(row)

    return table


def output():
    """
    Opens a output file and write the contents into it.

    Arguments:
              None

    Return:
          None
    """
    output_name = filename + ".out"
    output_file = open(output_name, 'w')

    # Writing to the output file, line by line
    for row in table:
        output_file.write(row + "\n")

    output_file.close()


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 freq.py". This is directly relevant to
    # this exercise, so you should call your code from here.
    extract_file()
    word_counter()
    output()
    pass
