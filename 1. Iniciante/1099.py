n = int(input())

for _ in range(n):
    x, y = input().split()

    x = int(x)
    y = int(y)

    count = [0]
    if x >= y:
        x, y = y, x

    for num in range(x + 1, y):
        if num % 2!= 0:
            count.append(num)

    print(sum(count))
      
