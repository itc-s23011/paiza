n = int(input())

words = []
for _ in range(n):
    word = input()
    words.append(word)

result = "_".join(words)
print(result)
