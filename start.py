from main import (
    split_expression,
    Notation,
    CalculateNotation
)
expression = '2 +3-4*5/6^7-(234,5^2/2)+(23-(23^3)+1000)/1^23'

if __name__ == "__main__":
    tokens = split_expression(expression)
    stack, notation = [], []

    if tokens:
        for token_ in tokens:
            element = Notation(token_, stack, notation)
            element.append_notation()
            stack = element.get_stack()
            notation = element.get_notation()

        while stack:
            notation.append(stack.pop())

        print(f"Polish notation = {' '.join(notation)}")

        for token_ in notation:
            element = CalculateNotation(token_, stack, [])
            element.calculate()
            stack = element.get_stack()

        print(f"Result = {stack[0]}")
