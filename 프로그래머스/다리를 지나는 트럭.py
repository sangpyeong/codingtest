#문제를 잘못읽음 최소를 구하라고해서 순서를 바꿔서 최소를 구하는 줄 알았는데 
#순서는 정해져 있고 최소값을 그대로 구하는 것으로 생각보다 쉬운 문제였음

from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.sort()
    q = deque()
    for i in range(bridge_length):
        q.appendleft(0)
    index = 0
    while(index < len(truck_weights)):
        q.pop()
        sum_weight=0
        for i in range(len(q)):
            sum_weight += q[i]
        
        if (sum_weight + truck_weights[index]) <= weight :
            q.appendleft(truck_weights[index])
            index+=1
        else:
            q.appendleft(0)
        answer+=1
    answer+=bridge_length
    
    return answer


from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights.sort()
    q = deque()
    for i in range(bridge_length):
        q.appendleft(0)
    while(truck_weights):
        q.pop()
        sum_weight=0
        for i in range(len(q)):
            sum_weight += q[i]
        posible_max_truck_weight=0
        index=0
        for i in range(len(truck_weights)):
            if sum_weight + truck_weights[i] <= weight:
                posible_max_truck_weight = max(posible_max_truck_weight, truck_weights[i])
                index = i
        if posible_max_truck_weight==0:
            q.appendleft(0)
        else:
            q.appendleft(posible_max_truck_weight)
            truck_weights.pop(index)  
        answer+=1
        print(q, answer)
    answer+=bridge_length
    
    return answer

#이게 정답
from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    q = deque()
    for i in range(bridge_length):
        q.append(0)
    index=0
    sum_weight=0
    while(index<len(truck_weights)):
        out_truck = q.pop()
        sum_weight-=out_truck
        if sum_weight + truck_weights[index] <= weight:
            q.appendleft(truck_weights[index])
            sum_weight+=truck_weights[index]
            index+=1
        else:
            q.appendleft(0)
        answer+=1
    answer+=bridge_length
    
    
    return answer