# 이번 과제는 전자 시계를 표현해봅니다:)

from datetime import datetime
import time

# 아래와 같이 0부터 9까지의 숫자(digit)을 표현할 수 있어요
#        ###         ###   ###         ###   ###   ###   ###   ### 
#       #   #     #     #     # #   # #     #         # #   # #   #
#       #   #     #     #     # #   # #     #         # #   # #   #
#       #   #     #     #     # #   # #     #         # #   # #   #
#                    ###   ###   ###   ###   ###         ###   ### 
#       #   #     # #         #     #     # #   #     # #   #     #
#       #   #     # #         #     #     # #   #     # #   #     #
#       #   #     # #         #     #     # #   #     # #   #     #
#        ###         ###   ###         ###   ###         ###   ### 


# 이 때 각 변을 0부터 6까지 숫자를 매겨서 그 변이 존재하면 True, 존재하지 않으면 False라고 할 때,
# digits 을 아래와 같이 정의할 수 있어요.
#   555  
#  4   0 
#  4   0 
#  4   0 
#   666  
#  3   1 
#  3   1 
#  3   1 
#   222  
digits = [[True, True, True, True, True, True, False],          # 0
            [True, True, False, False, False, False, False],    # 1
            [True, False, True, True, False, True, True],       # 2
            [True, True, True, False, False, True, True],       # 3
            [True, True, False, False, True, False, True],      # 4
            [False, True, True, False, True, True, True],       # 5
            [False, True, True, True, True, True, True],        # 6
            [True, True, False, False, False, True, False],     # 7
            [True, True, True, True, True, True, True],         # 8
            [True, True, True, False, True, True, True],        # 9
            [False, False, False, False, False, False, False]]  # Blank

# string digit, integer size, string c를 받아서 LCD 숫자 string을 리턴
# size는 display 크기, c는 display에 사용될 글자입니다.
# digit이 0-9에 해당하는 숫자 string이 아니면 blank string을 리턴해주세요.
# lcd_digit('0', 2, '*')
#  ** 
# *  *
# *  *
# 
# *  *
# *  *
#  ** 
# lcd_digit('4', 3, '&')
#
# &   &
# &   &
# &   &
#  &&& 
#     &
#     &
#     &
# 
# lcd_digit('9', 5, 'M')
#  MMMMM 
# M     M
# M     M
# M     M
# M     M
# M     M
#  MMMMM 
#       M
#       M
#       M
#       M
#       M
#  MMMMM 
# lcd_digit('a', 3, 'M')
#
#
#
#
#
#
#
#
#

def lcd_digit(digit, size, c):
    font=''
    shape_line=" "+c*size # ㅡ, 
    shape_left=("\n"+c)*size+"\n" #ㅣ 
    shape_right=("\n"+" "+" "*size+c)*size+"\n" #  ㅣ
    shape_double=("\n"+c+" "*size+c)*size+"\n" #ㅣ ㅣ
    blank_line=" "+" "*size #(ㅡ)
    blank_double=("\n"+" "+" "*size+" ")*size+"\n" #(ㅣ ㅣ)
    
    if digit not in ['0','1','2','3','4','5','6','7','8','9']:
        digit='10'

    digit = int(digit)
    font+=shape_line if digits[digit][5] else blank_line
        

    if digits[digit][4] and digits[digit][0]: # True, True
        font+=shape_double
    elif not digits[digit][4] and not digits[digit][0]: # False, False
        font+=blank_double
    elif digits[digit][4] and not digits[digit][0]: # True, False
        font+=shape_left
    else: # False, True
        font+=shape_right
    
    font+= shape_line if digits[digit][6] else blank_line
    

    if digits[digit][3] and digits[digit][1]:
        font+=shape_double
    elif not digits[digit][3] and not digits[digit][1]:
        font+=blank_double
    elif digits[digit][3] and not digits[digit][1]:
        font+=shape_left
    else:
        font+=shape_right

    font+=shape_line if digits[digit][2] else blank_line

    return font

# 다음으로는 두 digit을 합치는 함수 combine을 작성해주세요.
# left, right을 각각 "\n"으로 split한 다음 조각들을 합쳐서 다시 새로운 string을 만들어야 합니다
# combine("This\nis\nfun", "&", "Hello\nlcd\nclock!")
# This&Hello
# is&lcd
# fun&clock!
# combine(lcd_digit('0', 3, '*'), " # ", lcd_digit('9', 3, '@'))
#  ***  #  @@@ 
# *   * # @   @
# *   * # @   @
# *   * # @   @
#       #  @@@ 
# *   * #     @
# *   * #     @
# *   * #     @
#  ***  #  @@@ 
#
def combine(left, sep, right):
    ans=[f"{l}+{sep}+{r}" for l,r in zip(left.split("\n"),right.split("\n"))]
    
    return ans
  
# print(combine(lcd_digit('8', 3, '@'), " # ", lcd_digit('9', 3, '@')))

# 이제 주어진 String을 LCD-format으로 변환하는 함수가 필요합니다.
def lcd(s, size, c, sep):
  result = lcd_digit(s[0], size, c)
  for i in range(1, len(s)):
    result = combine(result, sep, lcd_digit(s[i], size, c))
  return result

# 이제 시간이 흐름에 따라 숫자를 바꿔봅시다
# 현재 시간을 가져와서 formatting하는 특별한 함수라 제공해드립니다.
def clear_screen():
  print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

def current_timestring():
    now = datetime.now()
    hour, minute, second = str(now.hour), str(now.minute), str(now.second)
    if len(hour) == 1: hour = "0" + hour
    if len(minute) == 1: minute = "0" + minute
    if len(second) == 1: second = "0" + second
    return "{0} {1} {2}".format(hour, minute, second)

def clock():
    current = current_timestring()
    clear_screen()
    print(lcd(current, 4, '#', " "))
    while True:
        time.sleep(1)
        ntime = current_timestring()
        if ntime != current:
            current = ntime
            clear_screen()
            print(lcd(current, 4, '#', " "))

# 이제 아래 코드의 주석을 지워서 시계를 run해보아요:)

#clock()



