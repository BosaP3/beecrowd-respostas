i = 0
j = 1

while i < 2:
    for _ in range(3):
        if i == 0 or i == 1 or i >= 1.8:
            print(f"I={i:.0f} J={j+(i):.0f}")
        else:
            print(f"I={i:.1f} J={j+(i):.1f}")

        j += 1

    i += 0.2
    j = 1
