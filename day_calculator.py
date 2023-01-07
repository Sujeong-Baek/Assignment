MONTH_LENGTH = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
LEAP_MONTH_LENGTH = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] # 윤년
FOUR_YEARS = 365 + 365 + 365 + 366

# 1901/01/01 부터 몇번째 date인지 return하는 함수
# date2num(1901, 01, 01) >> 0
# 1901 - 2099 년 사이의 date 에 대해서만 계산
# illegal한 input에 대해서는 return -1
# date2num(1901, 1, 1) >> 0
# date2num(1901, 2, 1) >> 31
# date2num(1901, 3, 1) >> 49
# date2num(1902, 3, 1) >> 424
# date2num(1902, 1, 1) >> 365
# date2num(2012, 2, 13) >> 40585
# date2num(2015, 3, 20) >> 41716
# date2num(2012, 2, 30) >> -1
# date2num(2012, 13, 1) >> -1
# date2num(2100, 4, 12) >> -1
def date2num(year, month, day):
    if year < 1901 or year > 2099 or month < 1 or month > 12:
        return -1
    is_leap = year % 4 == 0
    ml = LEAP_MONTH_LENGTH if is_leap else MONTH_LENGTH
    if day < 1 or day > ml[month-1]:
        return -1
    yearn = year - 1901
    monthn = month - 1
    dayn = day - 1
    
    total = 0
    total += FOUR_YEARS * (yearn // 4)
    total += 365 * (yearn % 4)
    for m in range(monthn):
        total += ml[m]
    total += dayn
    return total

# "YYYY/MM/DD" 형식의 s 가 주어질 때 (year, month, day)를 반환하도록 작성하세요.
# illegal한 형식에 대해서는 (0, 0, 0)을 리턴하세요.
# string2date("2010/02/12") >> (2010, 2, 12)
# string2date("1492/02/31") >> (1492, 2, 31)
# string2date("14a2/2/31") >> (0, 0, 0)
# string2date("14a2/02/31") >> (0, 0, 0)
def string2date(s):
    ymd=s.split("/")
    if len(ymd) != 3:
        return (0,0,0)
    year, month, day = ymd

    if not year.isdigit() or not month.isdigit() or not day.isdigit():
        return (0,0,0)
    return int(year), int(month), int(day)

# 함수 isdigit() 과 isnumeric()의 차이 알아보기


def date2string(year,month,day):
    y = str(year)
    m = "0" + str(month) if month < 10 else str(month)
    # m = str(month)
    # if month < 10:
    #     m = "0" + m
    d = "0" + str(day) if day < 10 else str(day)
    # return y + "/" + m + "/" + d
    # return "{0}/{1}/{2}".format(y, m, d)
    return '/'.join([y, m, d])

print(date2string(2010, 12, 2))




# integer n이 주어질 때 (year, month, day)를 반환하도록 작성하세요.
# num2date(0) >> (1901, 1, 1)
# num2date(31) >> (1901, 2, 1)
# num2date(59) >> (1901, 3, 1)
# num2date(424) >> (1902, 3, 1)
# num2date(365) >> (1902, 1, 1)
# num2date(40585) >> (2012, 2, 13)

def num2date(n):
    year=1901
    month=1
    day=1

    # q, r = divmod(n, FOUR_YEARS)
    year+=(n//FOUR_YEARS*4)+(n%FOUR_YEARS//365)
    
    length = MONTH_LENGTH if year%4 else LEAP_MONTH_LENGTH
    n=(n%FOUR_YEARS)%365
    for l in length:
        n-=l
        if n < 0:
            break
        month+=1
        day=n+1

    return year,month,day
    
# if a == 0:
#     return 'a'
# else:
#     return 'b'

# if a:
#     return 'b'
# else:
#     return 'a'


# "YYYY/MM/DD" 형식의 string date 가 input 으로 주어질 때 해당 date의 요일을 반환하세요.
# day("2017/03/20") >> "2017/03/20 is a Monday"
# day("2012/02/10") >> "2012/02/10 is a Friday"

def day(date):
    
    dows=["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"] 
    year,month,day=string2date(date)

    total=date2num(year, month, day)
    if total<0:
        return -1

    return date+' is a '+ dows[total%7]
    

# date=input()
# print(day(date))

#print(day(date))실행시 -1이 출력

# "YYYY/MM/DD" 형식의 string start, end 가 input으로 주어질 때 두 날짜 사이의 기간을 반환하세요.
# between("1992/03/21", "2017/03/20") >> "There are 9130 days between 1992/03/21 and 2017/03/20"
# between("2017/03/20", "2015/12/24") >> "There are -452 days between 2017/03/20 and 2015/12/24"
def between(start, end):

    syear,smonth,sday=string2date(start)  
    stotal=date2num(syear,smonth,sday)

    eyear,emonth,eday=string2date(end)
    etotal=date2num(eyear,emonth,eday)

    long=etotal-stotal
    howlong=('"'+'There are '+str(long)+' days between '+start+' and '+end)
    return howlong

# (start,end)=input('','')...?
# print(between(start, end))

print(between("1992/03/21", "2017/03/20"))

def intdate(date):
    ymd=string2date(date)
    year=ymd[0]
    month=ymd[1]
    day=ymd[2]

    tymd=(year,month,day)
    return tymd


def day2(date):
    
    dows=["Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday","Monday"] 
    
    ymd=intdate(date)
    total=date2num(ymd[0], ymd[1], ymd[2])
    if total<0:
        return -1
    else: dow=total%7

    whatday=('"'+date+' '+'is a'+' '+ dows[dow]+'"')
    return whatday


def between2(start, end):
    symd=intdate(start)
    stotal=date2num(symd[0],symd[1],symd[2])
    
    eymd=intdate(end)
    etotal=date2num(eymd[0],eymd[1],eymd[2])

    long=etotal-stotal
    howlong=('"'+'There are '+str(long)+' days between '+start+' and '+end)
    return howlong
 





# "YYYY/MM/DD" 형식의 string start, op는 "plus" 또는 "minus", end는 integer인 input일 때 두 날짜 사이의 기간을 반환하세요.
# calculate("2017/03/20", "minus", 100) >> "2017/03/20 minus 100 days = 2016/12/10"
# calculate("2017/03/20", "plus", 100) >> "2017/03/20 plus 100 days = 2017/06/28"
def calculate(start, op, end):
    ymd=intdate(start)
    total=date2num(ymd[0], ymd[1], ymd[2])

    if op == "minus":
        etotal=total-end
        enddate=num2date(etotal)
        e=date2string(enddate[0],enddate[1],enddate[2])
    elif op == "plus":
        etotal=total+end
        enddate=num2date(etotal)
        e=date2string(enddate[0],enddate[1],enddate[2])
    else: return -1

    plusminus=('"'+start+' '+op+' '+ str(end)+' days = '+e+'"')
    return plusminus

