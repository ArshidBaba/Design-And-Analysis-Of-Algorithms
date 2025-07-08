n = 6

d = {
    1: 1,
    2: 2,
    3: 3,
    # 4:5,
    # 5:8,
    # 6:12
}

for i in range(4, n + 1):
    keys = d.keys()
    key = d.values().index(d[i])
    d[i] = d[i - 1] + (key - 1)

print(d)
