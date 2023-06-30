def check_movie(s, n):
    if s >= n:
        return "OK"
    else:
        return "NG"


s, n = map(int, input().split())
result = check_movie(s, n)
print(result)
