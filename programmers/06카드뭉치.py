# https://school.programmers.co.kr/learn/courses/30/lessons/159994
def solution(cards1, cards2, goal):
    
    card1_index=find_cards_index(goal,cards1)
    card2_index=find_cards_index(goal,cards2)

    if len(card1_index)+len(card2_index)==len(goal):
        if check_over_index(card1_index) and check_over_index(card2_index):
            if check_sorted_list(card1_index) and check_sorted_list(card2_index):
                return "Yes"    
    return "No"
       


# goal에서 card와 일치한 index를 list로 return
def find_cards_index(goal,cards):
    card_index=[]
    for card in cards:
        for i in range(len(goal)):
            if card==goal[i]:
                card_index.append(i)
    return card_index

#카드를 중복사용했는지 확인하기
def check_over_index(card_index):
    for card in card_index:
        if card_index.count(card)>1:
            return False
    return True
            

#list를 정렬하여 정렬전 list와 일치한지
def check_sorted_list(index_list):
    return True if sorted(index_list)==index_list else False
