def energy_drink(c1, p1, c2, p2):
    ration1 = c1 / p1
    ration2 = c2 / p2

    if ration1 > ration2:
        return 1
    else:
        return 2


c1, p1 = map(int, input().split())
c2, p2 = map(int, input().split())


result = energy_drink(c1, p1, c2, p2)
print(result)
