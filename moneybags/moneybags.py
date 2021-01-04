# --------------------------------------------
# Name: Bhavnoor Kaur
# ID: 1623727
# CMPUT 274, Fall 2020
#
# Weekly Exercise 7: Dr MoneyBags
# --------------------------------------------

# importing required module
from bisect import bisect


def take_input():
    """ This function takes the input from the user and returns it.
    Arguments:
              None
    Returns:
            n - an integer entered by the user, which is the
                number of applicants to the club.
            applicants - A list containing integers, each of
                         which  describes the net worth of the
                         given applicant, in million dollars.
    """
    # taking the input for the number of applicants
    n = int(input())
    # storing the net worth of applicants in a list
    applicants = sorted([int(input()) for i in range(n)])

    return n, applicants


def min_wealth_threshold(n, applicants):
    """ This function takes the "n
    Arguments:
              n - an integer value
              applicants - A list containing the net worth
              of ech applicant
    Returns:
            min_threshold - an integer which is the minimum
            threshold
    """

    # initiating an empty list for the solution
    sol = []

    # calculating the count of people who atleast have
    # j million dollars, where j is between 0, n-1.
    for j in range(n):
        count = len(applicants) - bisect(applicants, j)
        # appending to list sol, if the atleast x people
        # have x million dollars.
        if j+1 <= count:
            sol.append(j+1)

    # returning the maximum from the list sol
    return max(sol)


def main():
    """ This function is the main function that calls
    the other functions
    Arguments:
              None
    Returns:
            None
    """

    n, applicants = take_input()
    N = min_wealth_threshold(n, applicants)
    print(N)


if __name__ == "__main__":
    # Any code indented under this line will only be run
    # when the program is called directly from the terminal
    # using python3 moneybags.py
    main()
