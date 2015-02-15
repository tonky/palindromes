import sys
import unittest
from tempfile import TemporaryFile
from palindrome import is_palindrome, parser, print_palindromes, parse_line


class TestPalindromes(unittest.TestCase):
    def test_palindrome(self):
        self.assertTrue(is_palindrome("testset"))
        self.assertTrue(is_palindrome("Azeeza"))
        self.assertTrue(is_palindrome("ma'am"))

    def test_not_palindrome(self):
        self.assertFalse(is_palindrome("testsets"))
        self.assertFalse(is_palindrome("a"))

    def test_parse_line(self):
        self.assertEquals(parse_line("Hey, dad! That ma'am is driving in her civic!"),
            ["dad", "ma'am", "civic"])

    def test_optparse(self):
        self.assertEquals(parser.description,
                "Detect and output palindromes in files.")

        assert("positional arguments:\n  input_file" in parser.format_help())

    def test_temp_file(self):
        with TemporaryFile('r+t') as tmp_file:
            tmp_file.write("I rode my kayak\nat noon\n\nbut ran out of food,\
                    ma'am.\nI hope to finish next Noon.")

            tmp_file.seek(0)

            count = print_palindromes(tmp_file)

            # gotta love the side effects
            output = sys.stdout.getvalue().strip()

            self.assertEquals(output, "kayak\nnoon\nma'am")
            self.assertEquals(len(count), 3)
            self.assertEquals(count["noon"], 2)


if __name__ == '__main__':
    # buffer stdout/stderr to catch the palindrome printing
    unittest.main(buffer=True)
