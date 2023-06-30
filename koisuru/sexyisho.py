def calculate_steps(M, N):
    total_steps = M - N
    if total_steps > 0:
        return total_steps
    else:
        return 0


M, N = map(int, input().split())
result = calculate_steps(M, N)
print(result)
