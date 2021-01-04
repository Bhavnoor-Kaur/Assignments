# -------------------------------------------------------------
# Name: Bhavnoor Kaur
# Student ID: 1623727
# CMPUT 274, Fall 2020
#
# Weekly Exercise 1 : Password Validator
# -----------------------------------------------------------
import random
import string


def validate(password):
    """ Analyzes an input password to determine if it is "Secure",
        "Insecure", or "Invalid" based on the assignment description criteria.

    Arguments:
        password (string): a string of characters

    Returns:
        result (string): either "Secure", "Insecure", or "Invalid".
    """
    loop_count = 0
    special = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")
    characters = list(password)
    # Check for the length of the password and the prohibited characters
    # for a secure password.
    if len(characters) < 8 or any(i in " @#" for i in characters) is True:
        return "Invalid"
    else:
        # In order to check for the presence of atleast one uppercase,
        # lowercase, decimal digit and the special character, the for loop
        # is selecting three characters from the list at a time and checking
        # for the uppercase, lowercase and digit through the if statement
        # We are also keeing a count of the number of times it is iterating
        # through the first for loop.
        for character_1 in characters:
            loop_count += 1
            for character_2 in characters:
                for character_3 in characters:
                    upper = character_1.isupper()
                    lower = character_2.islower()
                    numeric = character_3.isnumeric()
                    if upper is True and lower is True and numeric is True:
                        if any(i in special for i in characters) is True:
                            return "Secure"
                        else:
                            return "Insecure"
                    else:
                        # It should only return insecure when it has iterated
                        # through all the characters and didnot
                        # meet the criteria for the secure password.
                        # otherwise, it continues the loop
                        if loop_count == len(characters):
                            return "Insecure"
                        else:
                            continue
    pass


def generate(n):
    """ Generates a password of length n which is guaranteed to be Secure
        according to the given criteria.

    Arguments:
        n (integer): the length of the password to generate, n >= 8.

    Returns:
        secure_password (string): a Secure password of length n.
    """
    # Ensure that the password is only generated when n > 8
    if n >= 8:
        # Creating lists of uppercase, lowercase, decimal digits
        # special characters.
        uppercase_letters = list(string.ascii_uppercase)
        lowercase_letters = list(string.ascii_lowercase)
        digits = [i for i in range(10)]
        special_chars = list("!-$%&'()*+,./:;<=>?_[]^`{|}~")

        # Combining all the lists to make a pool of characters
        chars = uppercase_letters + lowercase_letters + digits + special_chars

        # Choosing a random uppercase, a lowercase, a digit
        # and a special character. Also, choosing the rest of the characters
        # from the pool.
        r_uppercase = list(chr(random.randint(65, 90)))
        r_lowercase = list(chr(random.randint(97, 122)))
        r_digit = list(chr(random.randint(48, 57)))
        r_special = list(random.choice("!-$%&'()*+,./:;<=>?_[]^`{|}~"))
        r_chars = random.choices(chars, k=n-4)

        # Combining all the randomly chosen characters
        # and shuffles them to mantain randomness
        password = r_chars + r_special + r_digit + r_lowercase + r_uppercase
        random.shuffle(password)
        # converting the list into a string
        secure_password = "".join(str(char) for char in password)
        return secure_password

    pass


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using "python3 validator.py". This can be useful for
    # testing your implementations.

    pass
