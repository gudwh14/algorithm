import collections


def solution(genres, plays):
    answer = []
    song = collections.defaultdict(list)
    total = collections.defaultdict(int)

    # 장르별 총합 구하고, 내림차순으로 정렬
    for i in range(0, len(genres)):
        total[genres[i]] += plays[i]
    total = sorted(total.items(), key=lambda x: x[1], reverse=True)

    # 장르별 음악 구분하여 저장하기
    for i in range(0, len(genres)):
        song[genres[i]].append([plays[i], i])

    # 장르별 음악 재생횟수로 내림차순으로 정렬
    for key in song:
        song[key].sort(key=lambda x: x[0], reverse=True)

    # 장르별 총합 순으로 각 장르에서 2개씩 가져오기
    for key, value in total:
        for count in range(0, 2):
            # 만약 장르의 노래 개수가 2개 보다 작을경우 break 해주기
            try:
                answer.append(song[key][count][1])
            except IndexError:
                break

    return answer


print(solution(["classic", "pop", "classic", "classic", "pop"], [500, 600, 150, 800, 2500]))
