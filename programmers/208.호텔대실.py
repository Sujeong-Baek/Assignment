# https://school.programmers.co.kr/learn/courses/30/lessons/155651
def solution(book_time):
    cleaned_time=add_cleaning(book_time)
    rooms=[cleaned_time[0][1]]
    for time in cleaned_time[1:]:
        found_room=False
        for i,room in enumerate(rooms):            
            if time[0]>=room:
                rooms[i]=time[1]
                found_room=True
                break
        if not found_room:
            rooms.append(time[1])

    return len(rooms)

def add_cleaning(book_time):
    book_time=sorted(book_time, key=lambda x: (x[0],x[1]))
    cleaned_time=[]
    for start,end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        end_m+=10
        end_h+=end_m//60
        cleaned_time.append([start_h*100+start_m, end_h*100+end_m%60])
    return cleaned_time