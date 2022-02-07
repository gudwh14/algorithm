def solution(m, musicinfos):
    # m 에 존재하는 # 치환해주기
    m = m.replace('C#', '1').replace('D#', '2').replace('E#', '3').replace('F#', '4').replace('G#', '5').replace('A#',
                                                                                                                 '6')
    # musicinfos 에 존재하는 # 치환하기
    for i in range(len(musicinfos)):
        musicinfos[i] = musicinfos[i].replace('C#', '1').replace('D#', '2').replace('E#', '3').replace('F#',
                                                                                                       '4').replace(
            'G#', '5').replace('A#', '6')

    musics = []
    # 해당 음악을 추출해서 [ 곡제목, 곡 총 음표, 곡 총 재생시간] 저장
    for music in musicinfos:
        # 스플릿
        music = music.split(',')
        # 시작시간 구하기
        start = int(music[0].split(':')[0]) * 60 + int(music[0].split(':')[1])
        # 끝나는 시간 구하기
        end = int(music[1].split(':')[0]) * 60 + int(music[1].split(':')[1])
        # 재생시간
        count = end - start
        # 곡 반복 횟수
        len_m = count // (len(music[3]))
        # 반복 하고 남은 수
        mod = count % (len(music[3]))
        # 음표
        sound = ''

        for _ in range(len_m):
            sound += music[3]

        for i in range(mod):
            sound += music[3][i]

        musics.append([music[2], sound, end - start])

    find_musics = []
    # m 음에 해당하는 곡찾기
    for idx, music in enumerate(musics):
        if m in music[1]:
            find_musics.append(music)

    if len(find_musics) >= 1:
        # 찾은 곡들을 재생시간 순으로 정렬하기
        find_musics.sort(key=lambda x: x[2], reverse=True)
        # 첫번째 값 출력
        return find_musics[0][0]
    return "(None)"


print(solution("ABCDEFG", ["12:00,12:14,HELLO,CDEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
print(solution("ABC", ["12:00,12:14,HELLO,C#DEFGAB", "13:00,13:05,WORLD,ABCDEF"]))
