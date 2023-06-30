def check_cd_recording(n, m, songs):
    total_time = 0
    max_songs = 0

    for t in songs:
        total_time += t
        if total_time <= n * 60:
            max_songs += 1
        else:
            break

    if max_songs == m:
        return "OK"
    else:
        return str(max_songs)


n = int(input())
m = int(input())

songs = []
for _ in range(m):
    t = int(input())  # 各曲の秒数
    songs.append(t)

result = check_cd_recording(n, m, songs)
print(result)
