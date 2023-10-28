# 내가 푼 풀이
def solution(genres, plays):
    answer = []
    genre_dict = {}

    for i, (genre, play) in enumerate(zip(genres, plays)):
        if genre not in genre_dict:
            genre_dict[genre] = [(i, play)]
        else:
            genre_dict[genre].append((i, play))

    h = []
    for k, v in genre_dict.items():
        total_play = sum(play for _, play in v)
        sorted_v = sorted(v, key=lambda x: (-x[1], x[0]))

        selected_songs = sorted_v[:2]

        h.append((total_play, selected_songs))

    h.sort(reverse=True, key=lambda x: x[0])

    for _, songs in h:
        for song in songs:
            answer.append(song[0])

    return answer

# 다른 사람 풀이


def solution(genres, plays):
    answer = []

    dic1 = {}
    dic2 = {}

    for i, (g, p) in enumerate(zip(genres, plays)):
        if g not in dic1:
            dic1[g] = [(i, p)]
        else:
            dic1[g].append((i, p))

        if g not in dic2:
            dic2[g] = p
        else:
            dic2[g] += p

    for (k, v) in sorted(dic2.items(), key=lambda x: x[1], reverse=True):
        for (i, p) in sorted(dic1[k], key=lambda x: x[1], reverse=True)[:2]:
            answer.append(i)

    return answer
