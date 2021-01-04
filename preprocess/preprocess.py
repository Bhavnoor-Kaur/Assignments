# --------------------------------------------
# Name: Bhavnoor Kaur
# ID: 1623727
# CMPUT 274, Fall 2020
#
# Weekly Exercise 4: Text Preprocessor
# --------------------------------------------
import sys
import string

global stopwords

# A list of all the stopwords
stopwords = ["i", "me", "my", "myself", "we", "our", "ours",
             "ourselves", "you", "your", "yours", "yourself", "yourselves",
             "he", "him", "his", "himself", "she", "her", "hers", "herself",
             "it", "its", "itself", "they", "them", "their", "theirs",
             "themselves", "what", "which", "who", "whom", "this", "that",
             "these", "those", "am", "is", "are", "was", "were", "be", "been",
             "being", "have", "has", "had", "having", "do", "does", "did",
             "doing", "a", "an", "the", "and", "but", "if", "or", "because",
             "as", "until", "while", "of", "at", "by", "for", "with",
             "about", "against", "between", "into", "through", "during",
             "before", "after", "above", "below", "to", "from", "up", "down",
             "in", "out", "on", "off", "over", "under", "again", "further",
             "then", "once", "here", "there", "when", "where", "why", "how",
             "all", "any", "both", "each", "few", "more", "most", "other",
             "some", "such", "no", "nor", "not", "only", "own", "same", "so",
             "than", "too", "very", "s", "t", "can", "will", "just", "don",
             "should", "now"]


def read_command():
    """
    This function assesing the command line arguments and returns
    mode specified by the user or prints out an error message
    if the command line argument is not valid.

    Arguments:
             None

    Returns:
           mode (string): the mode in which the user wants to run the program

    """
    global mode

    # A list of acceptable values of modes
    modes = ["keep-digits", "keep-stops", "keep-symbols", "normal"]

    # Asseses the second argument of the command line and assign its value to
    # the variable 'mode', if not present assigns a value of 'normal' to the
    # variable mode, for all other cases, print an error message
    if len(sys.argv) == 2:
        mode = sys.argv[1]
    elif len(sys.argv) == 1:
        mode = "normal"
    else:
        print("Error processing the command line argument.")
        print("The proper usage is:")
        print("python3 preprocess.py <mode>")
        print("where <mode> is the mode in which you want to run the program,")
        print("it is optional & can only have following values if present:")
        print("keep-digits, keep-stops, keep-symbols")
        sys.exit()

    # Returns mode if it has an acceptable value, otherwise it prints
    # out an error message.
    if mode in modes:
        return mode
    else:
        print("Error processing the command line argument.")
        print("The proper usage is:")
        print("python3 preprocess.py <mode>")
        print("where <mode> is the mode in which you want to run the program,")
        print("it is optional & can only have following values if present:")
        print("keep-digits, keep-stops, keep-symbols")
        sys.exit()


def preprocess():
    """
    This function process the words inputted by the user in accordance with
    the value of mode and then prints out a list of space separated processed
    words.

    Arguments:
              None

    Returns:
        None
    """

    # Takes the input from the user
    words = list(input().split())

    # Creates a list of alphabets and decimal digits
    characters = list(string.ascii_lowercase)
    numbers = [str(i) for i in range(10)]
    characters.extend(numbers)

    processed_words = []

    if mode == "normal":
        # Iterates through each word in the list
        for word in words:
            # converts to lowercase
            lower_word = word.lower()
            # Takes the characters in the word one by one and joins them except
            # the non alphanumeric characters
            alphanum = "".join([i for i in lower_word if i in characters])
            # Remove the digits from the word
            filtered_word = "".join([i for i in alphanum if not i.isdigit()])
            # if the word after removing digits is empty, it appends the
            # original alphanumeric word to the list
            if not filtered_word:
                processed_words.append(alphanum)
            else:
                processed_words.append(filtered_word)

        # Removes predefined stopwords from the list, if any present.
        for stopword in stopwords:
            for word in processed_words:
                if word == stopword:
                    processed_words.remove(stopword)

    elif mode == "keep-digits":
        # Iterates through each word in the list
        for word in words:
            # converts to lowercase
            lower_word = word.lower()
            # Takes the characters in the word one by one and joins them except
            # the non alphanumeric characters
            alphanum = "".join([i for i in lower_word if i in characters])
            processed_words.append(alphanum)

        # Removes predefined stopwords from the list, if any present.
        for stopword in stopwords:
            for word in processed_words:
                if word == stopword:
                    processed_words.remove(stopword)

    elif mode == "keep-symbols":
        # Iterates through each word in the list
        for word in words:
            # converts to lowercase
            lower_word = word.lower()
            # Remove the digits from the word
            filtered_word = "".join([i for i in lower_word if not i.isdigit()])
            # if the word after removing digits is empty, it appends the
            # original lower case word to the list
            if not filtered_word:
                processed_words.append(lower_word)
            else:
                processed_words.append(filtered_word)

        # Removes predefined stopwords from the list, if any present.
        for stopword in stopwords:
            for word in processed_words:
                if word == stopword:
                    processed_words.remove(stopword)

    elif mode == "keep-stops":
        # Iterates through each word in the list
        for word in words:
            # converts to lowercase
            lower_word = word.lower()
            # Takes the characters in the word one by one and joins them except
            # the non alphanumeric characters
            alphanum = "".join([i for i in lower_word if i in characters])
            # Remove the digits from the word
            filtered_word = "".join([i for i in alphanum if not i.isdigit()])
            # if the word after removing digits is empty, it appends the
            # original alphanumeric word to the list
            if not filtered_word:
                processed_words.append(alphanum)
            else:
                processed_words.append(filtered_word)

    # removes any empty strings present in the string
    while "" in processed_words:
        processed_words.remove("")

    # Prints a list of space separated processed words
    print(" ".join(processed_words))


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 preprocess.py". This is directly relevant
    # to this exercise, so you should call your code from here.
    read_command()
    preprocess()
