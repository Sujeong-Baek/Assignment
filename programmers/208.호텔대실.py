# https://school.programmers.co.kr/learn/courses/30/lessons/155651
def solution(book_time):
    int_book_time=change_int(book_time)
    rooms=[int_book_time[0][1]]
    
    for time in int_book_time[1:]:
        found_room=False
        for i,room in enumerate(rooms):
            if time[0]-room>=10:
                rooms[i]=time[1]
                found_room=True
                break
        if not found_room:
            rooms.append(time[1])

    return len(rooms)

def change_int(book_time):
    book_time=sorted(book_time, key=lambda x: (x[0],x[1]))
    int_book_time=[]
    for start,end in book_time:
        start_h, start_m = map(int, start.split(":"))
        end_h, end_m = map(int, end.split(":"))
        int_book_time.append([start_h*60+start_m, end_h*60+end_m])
    return int_book_time