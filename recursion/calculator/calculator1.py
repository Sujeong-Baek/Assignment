#
# Calculator, version 1
#
import tokens

class InputError(Exception):
    def __init__(self, msg, token):
        self.msg = msg
        self.token = token

# item: 숫자, 변수명, ()로 감싸진 expression
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
        raise InputError("Expected operator or ')'", t)
    tok.pop(0)
    return expr

# term: item의 product(*, /)
def parse_term(tok):
    result = parse_item(tok)
    t = tok[0]
    while t.isSymbol("*") or t.isSymbol("/"):
        tok.pop(0)
        rhs = parse_item(tok)
        if t.isSymbol("/"):
            result = result / rhs
        else:
            result = result * rhs
        t = tok[0]
    return result

# expression: term의 sum(+, -)
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

# 공백은 skip
# 숫자는 .을 포함할 수도 있는 string으로 구성
# identifier는 알파벳이나 _ 로 시작할 수 있고 알파벳, 숫자, _로 구성
# 나머지는 한 글자짜리 symbol token
def parse(s):
    toks = tokens.tokenize(s)
    result = parse_expression(toks)
    if not toks[0].isStop():
        raise InputError("Expected operator or end of input", toks[0])
    return result

# --------------------------------------------------------------------

if __name__ == "__main__":
    print("Welcome to Supercalculator v0.1")
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
# "2 + 3 * 4 / (3 + 2)"
# parse_expression -> parse_term -> parse_item -> parse_expression
