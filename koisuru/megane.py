N = int(input())
numbers = list(map(int, input().split()))
sorted_numbers = sorted(numbers, reverse=True)
middle_index = (N + 1) // 2
middle_number = sorted_numbers[middle_index - 1]
print(middle_number)
