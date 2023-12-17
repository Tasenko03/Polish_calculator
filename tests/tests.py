from main import *
import unittest


class MainFuncTests(unittest.TestCase):
    """
    Tests functions from main.py
    """

    def test_split_expression_float(self) -> None:
        """
        Checks float digits processing
        """
        self.assertEqual(split_expression('0,1'), split_expression('0.1'))

    def test_split_expression_spaces(self):
        """
        Checks blank spaces processing
        """
        actual = split_expression(' 3    +5   ')
        expected = ['3', '+', '5']
        self.assertEqual(actual, expected)

    def test_split_expression_basic(self):
        """
        Checks processing of every sign
        """
        actual = split_expression('3+4-2.5*3/(4^2)')
        expected = ['3', '+', '4', '-', '2.5', '*', '3', '/', '(', '4', '^', '2', ')']
        self.assertEqual(actual, expected)
