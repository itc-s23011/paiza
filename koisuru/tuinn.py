s = int(input())
t = int(input())

progress = "-" * s
progress_list = list(progress)
progress_list[t - 1] = "+"
result = "".join(progress_list)

print(result)
