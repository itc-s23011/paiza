n, p = map(int, input().split())
m, q = map(int, input().split())

required_paper = (n + m - 1) // m
total_cost = required_paper * q + n * p

print(total_cost)
