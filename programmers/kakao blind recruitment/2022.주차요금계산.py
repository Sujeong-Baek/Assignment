# https://school.programmers.co.kr/learn/courses/30/lessons/92341
from collections import defaultdict
from math import ceil

def create_car2record(records):
    car2record=defaultdict(list)    
    for record in records:
        time, car, _ = record.split()
        h,m=time.split(":")
        car2record[car].append(int(h)*60+int(m))
    return car2record

def cal_park_min(record):
    park_min=0
    while record:
        out_min=record.pop()
        in_min=record.pop()
        park_min+=out_min-in_min
    return park_min

def solution(fees, records):
    answer = []
    dmin, dfee, umin, ufee = fees
    records=sorted(records, key=lambda x: x.split()[1])
    car2record=create_car2record(records)
    
    for car in car2record:
        if len(car2record[car])%2:
            car2record[car].append(23*60+59)
            
        park_min=cal_park_min(car2record[car])       
        if park_min-dmin<=0:
            answer.append(dfee)
        else:
            answer.append(dfee + ceil((park_min - dmin)/umin) * ufee )
            
    return answer
