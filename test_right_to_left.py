import unittest

"""
# Melhor solução.

def left_join(phrases):
    return (",".join(phrases)).replace("right","left")
"""


def left_join(phrases):
    list_ = []
    for idx, word in enumerate(phrases):
        if 'right' in word:
            w = word.replace('right', 'left')
            list_.append(w)
        else:
            list_.append(word)

    return ",".join(str(x) for x in list_)


class MyTestCase(unittest.TestCase):
    def test_left_join01(self):
        self.assertEqual(left_join(("left", "right", "left", "stop")), "left,left,left,stop")  # "All to left"

    def test_left_join02(self):
        self.assertEqual(left_join(("bright aright", "ok")), "bleft aleft,ok")  # "Bright Left"

    def test_left_join03(self):
        self.assertEqual(left_join(("brightness wright",)), "bleftness wleft")  # "One phrase"

    def test_left_join04(self):
        self.assertEqual(left_join(("enough", "jokes")), "enough,jokes")  # "Nothing to replace"


if __name__ == '__main__':
    unittest.main()

"""
"For centuries, left-handers have suffered unfair discrimination in a world designed for right-handers."
Santrock, John W. (2008). Motor, Sensory, and Perceptual Development.
"Most humans (say 70 percent to 95 percent) are right-handed, a minority (say 5 percent to 30 percent) are left-handed, and an indeterminate number of people are probably best described as ambidextrous."
Scientific American. www.scientificamerican.com
One of robots is charged with a simple task: to join a sequence of strings in one sentence to produce instructions on how to get around the ship. But this robot is left-hander and has a tendency to joke around and confuse its right handed friends.

You are given a sequence of strings. You should join these strings into chunk of text where the initial strings are separated by commas. As a joke on the right handed robots, you should replace all cases of the words "right" with the word "left", even if it's a part of another word. All strings are given in lowercase.

Input: A sequence of strings as a tuple of strings (unicode).

Output: The text as a string.

Example:

left_join(("left", "right", "left", "stop")) == "left,left,left,stop"
left_join(("bright aright", "ok")) == "bleft aleft,ok"
left_join(("brightness wright",)) == "bleftness wleft"
left_join(("enough", "jokes")) == "enough,jokes"

1
2
3
4
5
How it is used: This is a simple example of operations using strings and sequences.

Precondition:
0 < len(phrases) < 42

"""
