# 어떤 해든 13일의 금요일을 포함하고 있다는걸 증명하는 문제입니다.

MONTH_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_MONTH_LENGTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년

# integer list month_days가 주어졌을 때 1/13, 2/13, 3/13, ..., 12/13 일이 몇 번째 일인지 리턴하는 함수를 작성하세요.
# day_number(MONTH_LENGTH) >> [12, 43, 71, 102, 132, 163, 193, 224, 255, 285, 316, 346]
# day_number(LEAP_MONTH_LENGTH) >> [12, 43, 72, 103, 133, 164, 194, 225, 256, 286, 317, 347]


def day_number(month_days):
    # for ml in MONTH_LENGTH:
    #     res.append(res[-1]+ml)
    # return res[:-1]
    res=[12]
    for ml in MONTH_LENGTH[:-1]:
        res.append(res[-1]+ml)
    return res

def day_number2(month_days):
    res = []
    acc = 12
    for day in MONTH_LENGTH:
        res.append(acc)
        acc += day
    return res

# integer list days 가 주어졌을 때 같은 요일(즉, day_number는 0부터 6까지의 수)이 몇 번 반복되는지 리턴하는 함수를 작성하세요.
# 일주일은 7일이기 때문에 이 함수는 7개의 integer를 포함하는 list를 리턴하고, i번째 element는 day number i 가 몇 번 나왔는지를 나타냅니다.
# week_days([0,1,3,5]) >> [1, 1, 0, 1, 0, 1, 0]
# week_days([0, 1, 3, 5, 8, 14, 21, 24]) >> [3, 2, 0, 2, 0, 1, 0]
# week_days([13, 20, 27, 34, 41, 48, 55]) >> [[0, 0, 0, 0, 0, 0, 7]

def week_days(days):
    ans=[0] * 7    
    for day in days :
        ans[day%7] += 1       
    return ans

#변수이름에 의미!!
#def안에는 return

