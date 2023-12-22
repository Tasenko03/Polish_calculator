"""
start.py
"""
from typing import Tuple

from src.main import (
    Notation,
    NotationCalculator,
    split_expression
)
MY_EXPRESSION = '5*(3-4^(3,5*2+(75+(2^8)-6)/(5,1+4203*0,1))' \
                '+567-(45.3-(32*(3.0+3,0)/6)/3)-1)/4'


def run(expression: str) -> Tuple[str, int] | Tuple[None, None]:
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
            element = NotationCalculator(token_, stack, [])
            element.calculate()
            stack = element.get_stack()

        return ''.join(' '.join(notation)), stack[0]
    return None, None


if __name__ == '__main__':
    polish_notation, result = run(MY_EXPRESSION)
    print(f'Polish notation = {polish_notation}')
    print(f'Result = {result}')
