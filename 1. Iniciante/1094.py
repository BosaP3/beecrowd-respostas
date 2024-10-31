n = int(input())

total = 0
coelhos= 0
sapos = 0  
ratos = 0

for i in range(n):
    quantia, tipo = input().split()

    if 'C' == tipo:
        coelhos += int(quantia)
    elif 'S' == tipo:
        sapos += int(quantia)
    elif 'R' == tipo:
        ratos += int(quantia)
    total += int(quantia)

print(f'Total: {total} cobaias')
print(f'Total de coelhos: {coelhos}')
print(f'Total de ratos: {ratos}' )
print(f'Total de sapos: {sapos}' )
print(f'Percentual de coelhos: %.2f' %float(((100*coelhos)/total)),'%')
print(f'Percentual de ratos: %.2f' %float(((100*ratos)/total)),'%')
print(f'Percentual de sapos: %.2f' %float(((100*sapos)/total)),'%')
