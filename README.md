[![CI](https://github.com/Tasenko03/Polish_calculator/actions/workflows/checks.yml/badge.svg)](https://github.com/Tasenko03/Polish_calculator/actions/workflows/checks.yml)
![pylint Score](https://mperlet.github.io/pybadge/badges/10.00.svg)

# Polish notation calculator

The program can convert any expression written in infix notation to reverse Polish notation. The input expression can contain: `- + / * ^ ( )`, as well as nested parentheses.
The program is able to evaluate an expression written in postfix notation and output the result of the expression.

## Classes interaction

The initial expression written in infix is accepted from the user and split into separate tokens using the `split_expression` function. 

### Notation
The `Notation` class accepts token, stack and notation (where elements of reverse Polish notation will be added). As a result, this class returns a finished expression (`notation`) written in reverse Polish notation using the `get_notation` method. 

### NotationCalculator
The `NotationCalculator` class is inherited from the `Notation` class. This class accepts token (element in `notation`) and stack. The `NotationCalculator` class evaluates an expression written in reverse Polish notation.  The computation is written to the stack. Finally, the class returns the result of the expression using the `get_stack` method, which is inherited from the parent class.