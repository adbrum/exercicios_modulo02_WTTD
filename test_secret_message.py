import unittest

"""
# Melhor solução.

find_message = lambda text: ''.join(filter(str.isupper, text))

"""


def find_message(text):
    word = ''
    for w in text:
        if w.isupper():
            word += w

    return word


class MyTestCase(unittest.TestCase):
    def test_find_message01(self):
        self.assertEqual(find_message("How are you? Eh, ok. Low or Lower? Ohhh."), "HELLO")

    def test_find_message02(self):
        self.assertEqual(find_message("hello world!"), "")

    def test_find_message03(self):
        self.assertEqual(find_message("HELLO WORLD!!!"), "HELLOWORLD")


if __name__ == '__main__':
    unittest.main()

"""
"Where does a wise man hide a leaf? In the forest. But what does he do if there is no forest? ... He grows a forest to hide it in."
-- Gilbert Keith Chesterton

Ever tried to send a secret message to someone without using the postal service? You could use newspapers to tell your secret. Even if someone finds your message, it’s easy to brush them off and that its paranoia and a bogus conspiracy theory. One of the simplest ways to hide a secret message is to use capital letters. Let's find some of these secret messages.

You are given a chunk of text. Gather all capital letters in one word in the order that they appear in the text.

For example: text = "How are you? Eh, ok. Low or Lower? Ohhh.", if we collect all of the capital letters, we get the message "HELLO".

Input: A text as a string (unicode).

Output: The secret message as a string or an empty string.

Example:

find_message("How are you? Eh, ok. Low or Lower? Ohhh.") == "HELLO"
find_message("hello world!") == ""

1
2
3
How it is used: This is a simple exercise in working with strings: iterate, recognize and concatenate.

Precondition: 0 < len(text) ≤ 1000
all(ch in string.printable for ch in text)
"""
