"""
tests.py
"""
import unittest

from src.main import split_expression


class MainFuncTests(unittest.TestCase):
    """
    Tests functions from main.py
    """

    def test_split_expression_float(self) -> None:
        """
        Checks float digits processing
        """
        self.assertEqual(split_expression('0,1'), split_expression('0.1'))

    def test_split_expression_spaces(self) -> None:
        """
        Checks blank spaces processing
        """
        actual = split_expression(' 3    +5   ')
        expected = ['3', '+', '5']
        self.assertEqual(actual, expected)

    def test_split_expression_basic(self) -> None:
        """
        Checks processing of every sign
        """
        actual = split_expression('3+4-2.5*3/(4^2)')
        expected = ['3', '+', '4', '-', '2.5', '*', '3', '/', '(', '4', '^', '2', ')']
        self.assertEqual(actual, expected)