import unittest

"""
# Outra solução.

def end_of_other(words):

    for w1 in words:
        for w2 in words:
            if w1 != w2 and (w1.endswith(w2) or w2.endswith(w1)):
                return True
    return False
"""


def end_of_other(words):
    for word1 in words:
        for word2 in words:
            if not (word1 == word2) and (word1.endswith(word2)):
                return True
    return False


class MyTestCase(unittest.TestCase):
    def test_end_of_other_true(self):
        self.assertEqual(end_of_other({"hello", "lo", "he"}), True)

    def test_end_of_other_false(self):
        self.assertEqual(end_of_other({"hello", "la", "hellow", "cow"}), False)

    def test_end_of_other_true02(self):
        self.assertEqual(end_of_other({"walk", "duckwalk"}), True)

    def test_end_of_other_false02(self):
        self.assertEqual(end_of_other({"one"}), False)

    def test_end_of_other_false03(self):
        self.assertEqual(end_of_other({"helicopter", "li", "he"}), False)


if __name__ == '__main__':
    unittest.main()

"""
For language training our Robots want to learn about suffixes.

In this task, you are given a set of words in lower case. Check whether there is a pair of words, such that one word
is the end of another (a suffix of another). For example: {"hi", "hello", "lo"} -- "lo" is the end of "hello",
so the result is True.

Input: Words as a set of strings.

Output: True or False, as a boolean.

Example:

checkio({"hello", "lo", "he"}) == True
checkio({"hello", "la", "hellow", "cow"}) == False
checkio({"walk", "duckwalk"}) == True
checkio({"one"}) == False
checkio({"helicopter", "li", "he"}) == False

1
2
3
4
5
6
How it is used: Here you can learn about iterating through set type and string data type functions.

Precondition: 2 ≤ len(words) < 30
all(re.match(r"\A[a-z]{1,99}\Z", w) for w in words)
"""
