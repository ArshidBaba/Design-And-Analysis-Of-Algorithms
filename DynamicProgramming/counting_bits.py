n = 5
ans = ["0"]
i = 1

while i <= n:
    m = i
    rem = 1
    while m != 0:
        print(m)
        # rem = rem * 10
        rem = rem + (m % 2) * 10
        m = m // 2

    ans.append(str(rem))
    i += 1

print(ans)
