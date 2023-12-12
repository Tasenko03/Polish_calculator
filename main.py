from typing import Optional, Any


def split_expression(raw_expression: str) -> Optional[list[str]]:
    """Function splits expression given from the user"""

    numbers = []
    new_expression = []

    for elem in raw_expression:
        if elem.isdigit() or elem == '.':
            numbers.append(elem)
        elif elem == ',':
            numbers.append('.')
        elif elem in ['+', '-', '*', '/', '^', '(', ')']:
            if numbers:
                new_expression.append("".join(numbers))
                numbers.clear()
            new_expression.append(elem)
        elif elem == ' ':
            pass
        else:
            print(f'{elem} is incorrect in your expression\nPlease, try again')
            return None

    new_expression.append("".join(numbers))
    return new_expression


class Notation:
    """Makes polish notation from original expression"""

    def __init__(self, token: str, stack_: list[Any], notation_: list[str]) -> None:
        """Initializes class Notation"""
        self._stack = stack_
        self.notation = notation_
        self.token = token
        self._signs = ['+', '-', '*', '/', '^']
        self._power_of_sign = {'-': 1, '+': 1, '*': 2, '/': 2, '^': 3}

    def power_of_signs(self, sign: str) -> int:
        """Returns the power of sign"""
        return self._power_of_sign.get(sign, 0)

    def append_notation(self) -> None:
        """Appends polish notation"""
        if self.token.isdigit() or self.token.replace('.', '').isdigit():
            self.notation.append(self.token)
        elif self.token in self._signs:
            while self._stack and self.power_of_signs(self._stack[-1]) >= self.power_of_signs(self.token):
                self.notation.append(self._stack.pop())
            self._stack.append(self.token)
        elif self.token == "(":
            self._stack.append(self.token)
        elif self.token == ")":
            while self._stack and self._stack[-1] != "(":
                self.notation.append(self._stack.pop())
            self._stack.pop()

    def get_notation(self) -> list[str]:
        """Returns notation"""
        return self.notation

    def get_stack(self) -> list[str]:
        """Returns stack"""
        return self._stack


class CalculateNotation(Notation):
    """Calculates polish notation"""

    def operation(self, operand1: float, operand2: float) -> float:
        """Returns the operation needed to calculate depending on the sign"""
        if self.token == '+':
            return operand1 + operand2
        elif self.token == '-':
            return operand1 - operand2
        elif self.token == '*':
            return operand1 * operand2
        elif self.token == '/':
            return operand1 / operand2
        elif self.token == '^':
            return operand1 ** operand2

    def calculate(self) -> None:
        if self.token.isdigit() or self.token.replace('.', '').isdigit():
            self._stack.append(float(self.token))
        elif self.token in self._signs:
            operand_2 = self._stack.pop()
            operand_1 = self._stack.pop()
            result = self.operation(operand_1, operand_2)
            self._stack.append(result)
