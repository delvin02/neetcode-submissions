class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operators = "+-/*"
        res = []

        for token in tokens:
            if token not in operators:
                res.append(int(token))

            match token:
                case "+":
                    res.append(res.pop() + res.pop())
                case "-":
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(num2 - num1)
                case "*":
                    res.append(res.pop() * res.pop())
                case "/":
                    num1 = res.pop()
                    num2 = res.pop()
                    res.append(math.trunc(num2/num1))

        return res[0]