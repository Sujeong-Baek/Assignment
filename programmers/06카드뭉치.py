from collections import deque
# https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(cards1, cards2, goal):
    cards1 = deque(cards1)
    cards2 = deque(cards2)
    goal = deque(goal)
    while goal:
        g = goal.popleft()
        one = cards1 and cards1[0] == g
        two = cards2 and cards2[0] == g
        if one and two:
            result1 = solution(cards1[1:], cards2, goal)
            if result1 == "Yes":
                return "Yes"
            return solution(cards1, cards2[1:], goal)
        elif one:
            cards1.popleft()
        elif two:
            cards2.popleft()
        else:
            return "No"
           
    return "Yes"

# lst.pop()
# lst.append()
# ["B"],["B", "C"],["B", "C", "B"]