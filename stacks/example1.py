from stack import print_stack


def first(n):
    second(n)
    second(n * n)


def second(m):
    three(m)
    three(m+1)
    three(m+2)


def three(z):
    print("In three(%d):" % z)
    print_stack()

def f1(n):
    f1(n+1)

f1(1)