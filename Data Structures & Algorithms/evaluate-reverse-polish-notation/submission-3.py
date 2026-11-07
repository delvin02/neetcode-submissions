import operator 
ops = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": lambda a,b: math.trunc(a/b)
}

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operands = []

        for s in tokens:
            if s not in ops:
                operands.append(int(s))
            else:
                num1 = operands.pop()
                num2 = operands.pop()
                res = self.calculate(s, num2, num1)
                operands.append(res)

        return operands[0]

    def calculate(self, op_string, num1, num2):
        op_func = ops.get(op_string)
        if op_func:
            return op_func(num1, num2)
        else:
            raise ValueError(f"Unsupported operator: {op_string}")