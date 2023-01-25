# 4 x 4 integer list이고 0은 empty를 나타냅니다
class Board:
    def __init__(self):
        pass

    # board를 출력했을 때의 나타날 string을 리턴해야합니다
    def __str__(self):
        pass

    # empty cell을 random하게 골라서 2 또는 4로 세팅합니다
    def insert():
        pass

    # 각각의 row에 대해 실행합니다
    # empty 가 아닌 cell을 가능한 한 왼쪽으로 옮깁니다.
    # ex. 0 2 0 4 >> 2 4 0 0
    # 같은 숫자의 cell을 만나면 merge합니다
    # ex. 0 2 0 2 >> 4 0 0 0
    # 해당 push에서 merge된 cell은 해당 차수에서 다시 merge할 수 없습니다
    # ex. 0 2 2 4 >> 4 4 0 0
    # 두 cell이 merge할 때마다 새로 생긴 cell 값을 포인트로 얻습니다
    def push_left():
        pass

    def push_right():
        pass

    def push_up():
        pass

    def push_down():
        pass

    def push(self, direction):
        if direction == 'l':
            return self.push_left()
        elif direction == 'r':
            return self.push_right()
        elif direction == 'u':
            return self.push_up()
        else:
            return self.push_down()

    # empty cell이 없다면 True를 리턴하고, 그 외엔 False를 리턴합니다
    def is_full():
        pass

# >>> val b = Board()
# >>> b
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o

# >>> b.insert()
# >>> b.insert()
# >>> b
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |  2 |    |    |
# |    |    |    |    |
# o----o----o----o----o
# |    |    |    |    |
# |    |    |    |  2 |
# |    |    |    |    |
# o----o----o----o----o

def main():
    b = Board()
    b.insert()
    b.insert()

    points = 0
    
    while True:
        print(b)
        print(f"{points} points\n")
        s = input("What is your move: ").lower().strip()
        print()
        if len(s) == 1 and s in "lrud":
            points += b.push(s[0])
        if b.is_full():
            print(b)
            print("\nGame over.")
            print(f"You have {points} points.")
            return
        b.insert()