#
# Calculator
#

# 1. math.pi, math.e를 이용해서 pi, e를 구현하세요
# Enter an expression: pi
# ==> 3.14159
# Enter an expression: 2 * pi
# ==> 6.28319
# Enter an expression: e
# ==> 2.71828
# Enter an expression: e^2
# ==> 7.38906
# Enter an expression: 1 - e^-1
# ==> 0.632121

# 2. 0 으로 나누려고 할 때 `Division by zero` 에러를 던지게 변경하세요
# 어디서 에러가 났는지 표시해야합니다
# Enter an expression: 4.5 / 0
# Error: Division by zero
# 4.5 / 0
#     ^
# Enter an expression: 1 + 2 + 3 + 4 / (10 - 2 * 5)
# Error: Division by zero
# 1 + 2 + 3 + 4 / (10 - 2 * 5)

# 3. 절댓값 연산을 추가하세요. 2개의 | 로 이루어져 있습니다
# 절댓값을 구하기 위해 `abs` 함수를 사용하세요.
# Enter an expression: |17|
# ==> 17
# Enter an expression: |-17|
# ==> 17
# Enter an expression: 3 + |34 - 76|
# ==> 45
# Enter an expression: -2 + |-2|
# ==> 0
# Enter an expression: |1374 - 2746|
# ==> 1372
# Enter an expression: 9 - |1 - |9 - 3 * 4||
# ==> 7

import tokens

class InputError(Exception):
    def __init__(self, msg, token):
        self.msg = msg
        self.token = token

def parse_item(tok):
    t = tok[0]
    tok.pop(0)
    if t.isNumber():
        return t.value
    if t.isIdentifier():
        raise InputError("Variables not yet implemented", t)
    if not t.isSymbol("("):
        raise InputError("Expected number, variable, or '('", t)
    expr = parse_expression(tok)
    if not tok[0].isSymbol(")"):
        raise InputError("Expected operator or ')'", tok[0])
    tok.pop(0)
    return expr

def parse_factor(tok):
    t = tok[0]
    sign = -1 if t.isSymbol("-") else +1
    if t.isSymbol("+") or sign < 0:
        tok.pop(0)
    result = parse_item(tok)
    while tok[0].isSymbol("^"):
        tok.pop(0)
        rhs = parse_factor(tok)
        result = result ** rhs
    return sign * result
  
def parse_term(tok):
    result = parse_factor(tok)
    t = tok[0]
    while t.isSymbol("*") or t.isSymbol("/"):
        tok.pop(0)
        rhs = parse_factor(tok)
        if t.isSymbol("/"):
            result = result / rhs
        else:
            result = result * rhs
        t = tok[0]
    return result

def parse_expression(tok):
    result = parse_term(tok)
    t = tok[0]
    while t.isSymbol("+") or t.isSymbol("-"):
        tok.pop(0)
        rhs = parse_term(tok)
        if t.isSymbol("+"):
            result = result + rhs
        else:
            result = result - rhs
        t = tok[0]
    return result

def parse(s):
    toks = tokens.tokenize(s)
    result = parse_expression(toks)
    if not toks[0].isStop():
        raise InputError("Expected operator or end of input", toks[0])
    return result

# --------------------------------------------------------------------

if __name__ == "__main__":
    print("Welcome to Supercalculator v0.2")
    while True:
        s = input("Enter an expression: ")
        if s is None or s.strip() == "":
            break
        try:
            value = parse(s)
            print("==> %g" % value)
        except InputError as e:
            print("Error:", e.msg)
            print(s)
            print(" " * e.token.pos + "^")

# --------------------------------------------------------------------
