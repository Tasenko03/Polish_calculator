"""
tests.py
"""
import unittest

from src.main import split_expression
from src.start import run


class FuncTests(unittest.TestCase):
    """
    Tests functions from main.py and start.py
    """

    def test_split_expression_wrong_input(self) -> None:
        """
        Checks function raises ValueError with wrong input
        """
        expression = '     7 % 3'
        with self.assertRaises(ValueError):
            split_expression(expression)

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

    def test_run_wrong_input(self) -> None:
        """
        Checks run() raises ValueError with wrong input
        """
        expression = ' 7 + hi - 3'
        with self.assertRaises(ValueError):
            run(expression)

    def test_run_float_comma_equals_point(self) -> None:
        """
        Checks run() equally processes floats with point and comma
        """
        expression = '2,5'
        actual = run(expression)
        expected = run('2.5')
        self.assertEqual(actual, expected)

    def test_run_basic(self) -> None:
        """
        Checks run() from start.py
        """
        expression = '5*(3-4^(3,5*2+(75+(2^8)-6)/(5,1+4203*0,1))' \
                     '+567-(45.3-(32*(3.0+3,0)/6)/3)-1)/4'
        actual = run(expression)
        expected = (
            '5 3 4 3.5 2 * 75 2 8 ^ + 6 - 5.1 4203 0.1 * + / + ^ - '
            '567 + 45.3 32 3.0 3.0 + * 6 / 3 / - - 1 - * 4 /',
            -58392.37042271247
        )
        self.assertEqual(actual, expected)

    def test_run_many_parentheses(self) -> None:
        """
        Checks run() can handle expressions with many parentheses
        """
        expression = '2+(3/(4+(6*(7-(9+2^6))))/2)^2'
        actual = run(expression)
        expected = (
            '2 3 4 6 7 9 2 6 ^ + - * + / 2 / 2 ^ +',
            2.0000146423365264
        )
        self.assertEqual(actual, expected)
