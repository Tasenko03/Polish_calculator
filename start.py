"""
start.py
"""
from typing import Tuple

from main import (
    CalculateNotation,
    Notation,
    split_expression
)
my_expression = '2 +3-4*5/6^7-(234,5^2/2)+(23-(23^3)+1000)/1^23'


def run(expression: str) -> Tuple[str, int]:
    """
    Makes polish notation from expression and returns it with the result
    """
    tokens = split_expression(expression)
    stack: list = []
    notation: list = []

    if tokens:
        for token_ in tokens:
            element = Notation(token_, stack, notation)
            element.append_notation()
            stack = element.get_stack()
            notation = element.get_notation()

        while stack:
            notation.append(stack.pop())

        for token_ in notation:
            element = CalculateNotation(token_, stack, [])
            element.calculate()
            stack = element.get_stack()

    return ' '.join(' '.join(notation)), stack[0]


if __name__ == "__main__":
    polish_notation, result = run(my_expression)
    print(f"Polish notation = {polish_notation}")
    print(f"Result = {result}")
