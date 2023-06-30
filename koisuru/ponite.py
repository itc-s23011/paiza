inputs = [input().split() for _ in range(5)]


def check_pass(inputs):
    for i in range(5):
        direction = inputs[i][0]
        expected_direction = inputs[i][1]

        if direction != expected_direction:
            return "NG"

    return "OK"


result = check_pass(inputs)
print(result)
