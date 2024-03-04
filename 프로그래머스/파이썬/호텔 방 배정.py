import sys
sys.setrecursionlimit(10**6)


def solution(k, room_number):
    answer = []
    room_dict = {}

    def find(room):
        if room not in room_dict:
            room_dict[room] = room + 1
            return room
        empty_room = find(room_dict[room])
        room_dict[room] = empty_room + 1
        return empty_room

    for i, v in enumerate(room_number):
        empty_room = find(v)
        answer.append(empty_room)

    return answer
