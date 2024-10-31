while True:
    m, n = map(int, input().split())
    if m <= 0 or n <= 0:
        break

    print(
        *range(min(m, n), max(m, n) + 1),
        sep=" ",
        end=" Sum=" + str(sum(range(min(m, n), max(m, n) + 1))),
    )
    print()
