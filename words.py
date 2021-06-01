"""For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!

Turn that into a function, print_upper_words. Test it out. (Don’t forget to add a docstring to your function!)

Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase).

Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters.

For example:

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})"""


def print_upper_words(words):
    """For a list of words, print out each word on a separate line, but in all uppercase. How can you change a word to uppercase? Ask Python for help on what you can do with strings!"""

    for word in words:
        print(word.upper())


def print_upper_words1(words):
    """Change that function so that it only prints words that start with the letter ‘e’ (either upper or lowercase)."""

    for word in words:
        if word.startswith("E") or word.startswith("e"):
            print (word.upper())

def print_upper_words2(words, must_start_with):
    """Make your function more general: you should be able to pass in a set of letters, and it only prints words that start with one of those letters."""

    for word in words:
        for letter in must_start_with:
            if word.startswith(letter):
                print (word.upper())

words = ["hello", "hey", "goodbye", "yo", "yes", "echo"]

print_upper_words(words) # all words are uppercase

print_upper_words1(words) #  ECHO

print_upper_words2(words, ["h", "y"]) # print "HELLO", "HEY", "YO", and "YES"
