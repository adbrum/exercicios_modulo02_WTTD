import unittest

"""
# Melhor solução.

from string import ascii_lowercase
​
def check_pangram(text):
    return set(ascii_lowercase).issubset(set(text.lower()))
"""


def check_pangram(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    for letter in alphabet:
        if letter in text.lower():
            continue
        else:
            return False
    return True


class MyTestCase(unittest.TestCase):
    def test_check_pangram_true(self):
        self.assertTrue(check_pangram("The quick brown fox jumps over the lazy dog."), "lazy dog")

    def test_check_pangram_false(self):
        self.assertFalse(check_pangram("ABCDEF"), "ABC")

    def test_check_pangram_true02(self):
        self.assertTrue(check_pangram("Bored? Craving a pub quiz fix? Why, just come to the Royal Oak!"), "Bored?")


if __name__ == '__main__':
    unittest.main()

"""
A pangram (Greek:παν γράμμα, pan gramma, "every letter") or holoalphabetic sentence for a given alphabet is a sentence
using every letter of the alphabet at least once. Perhaps you are familiar with the well known pangram "The quick brown
fox jumps over the lazy dog".

For this mission, we will use the latin alphabet (A-Z). You are given a text with latin letters and punctuation symbols.
You need to check if the sentence is a pangram or not. Case does not matter.

Input: A text as a string.

Output: Whether the sentence is a pangram or not as a boolean.

Example:

check_pangram("The quick brown fox jumps over the lazy dog.") == True
check_pangram("ABCDEF.") == False
1
2
How it is used: Pangrams have been used to display typefaces, test equipment, and develop skills in handwriting,
calligraphy, and keyboarding for ages.

Precondition:

all(ch in (string.punctuation + string.ascii_letters + " ") for ch in text)
0 < len(text)
"""
