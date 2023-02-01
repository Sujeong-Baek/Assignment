import random
# 4 x 4 integer list이고 0은 empty를 나타냅니다
class Board:
    def __init__(self):
        self.nums =[[0]*4 for _ in range(4)]

    # board를 출력했을 때의 나타날 string을 리턴해야합니다
    def __str__(self):
        line = ""
        top="o----o----o----o----o\n"
        side = "|    |    |    |    |\n"
        for i in range(4):
            line+=top+side+"|"
            for j in self.nums[i]:
                if j==0: j=" "
                line += f'{j:^4}|'
            line += "\n"+side
        return line+top    

    # empty cell을 random하게 골라서 2 또는 4로 세팅합니다
    def insert(self):
        while True:
            x=random.randrange(4)
            y=random.randrange(4)
            num=self.nums[x][y]
            if num == 0:
                num=random.choice([2,4])
                self.nums[x][y]=num
                return

    # 각각의 row에 대해 실행합니다
    # empty 가 아닌 cell을 가능한 한 왼쪽으로 옮깁니다.
    # ex. 0 2 0 4 >> 2 4 0 0
    # 같은 숫자의 cell을 만나면 merge합니다
    # ex. 0 2 0 2 >> 4 0 0 0
    # 해당 push에서 merge된 cell은 해당 차수에서 다시 merge할 수 없습니다
    # ex. 0 2 2 4 >> 4 4 0 0
    # 두 cell이 merge할 때마다 새로 생긴 cell 값을 포인트로 얻습니다
    def push_left(self):
        point=0
        for i in range(4):
            left=[0,0,0,0]
            pos=0
            pre=0
            for j in range(4):
                if not self.nums[i][j]:
                    continue
                if pre!=self.nums[i][j]:
                    left[pos]=self.nums[i][j]
                    pre=self.nums[i][j]
                    pos+=1
                else:
                    left[pos-1]=pre*2
                    point+=pre*2
                    pre=0
            self.nums[i]=left
        return point

    def push_right(self):
        point=0
        for i in range(4):
            right=[0,0,0,0]
            pos=3
            pre=0
            for j in range(3,-1,-1):
                if not self.nums[i][j]:
                    continue
                if pre!=self.nums[i][j]:
                    right[pos]=self.nums[i][j]
                    pre=self.nums[i][j]
                    pos-=1
                else:
                    right[pos+1]=pre*2
                    point+=pre*2
                    pre=0
            self.nums[i]=right
    
        return point


    def push_up(self):
        point=0
        up=[[0]*4 for _ in range(4)]
        pos_x=0
        for i in range(4):
            pos_y=0
            pre=0
            for j in range(4):
                if not self.nums[j][i]:
                    continue
                if pre!=self.nums[j][i]:
                    up[pos_y][pos_x]=self.nums[j][i]
                    pre=self.nums[j][i]
                    pos_y+=1
                else:
                    up[pos_y-1][pos_x]=pre*2
                    point+=pre*2
                    pre=0
            pos_x+=1
        self.nums=up
        return point
            

    def push_down(self):
        point=0
        down=[[0]*4 for _ in range(4)]
        pos_x=0
        for i in range(4):
            pos_y=3
            pre=0
            for j in range(3,-1,-1):
                if not self.nums[j][i]:
                    continue
                if pre!=self.nums[j][i]:
                    down[pos_y][pos_x]=self.nums[j][i]
                    pre=self.nums[j][i]
                    pos_y-=1
                else:
                    down[pos_y+1][pos_x]=pre*2
                    point+=pre*2
                    pre=0
            pos_x+=1
        self.nums=down
        return point
        
        

    def push(self, direction):
        if direction == 'l':
            return self.push_left()
        elif direction == 'r':
            return self.push_right()
        elif direction == 'u':
            return self.push_up()
        else:
            return self.push_down()



    # empty cell이 없?다면 True를 리턴하고, 그 외엔 False를 리턴합니다
    def is_full(self):
        for i in range(4):
            for j in range(4):
                if 0 == self.nums[i][j]:
                    return False
        return True


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
    
    points=0

    while True:
        print(b)
        print(f"{points} points\n")
        s = input("What is your move: ").lower().strip()
        print()
        if len(s) != 1 or not s in "lrud":
            continue
        if len(s) == 1 and s in "lrud":
            pre=b.nums.copy()
            points+=b.push(s)
            if pre!=b.nums:
                b.insert()
         
        if b.is_full():
            print(b)
            print("\nGame over.")
            print(f"You have {points} points.")
            return
        

