# break em while
total = 0
while (True):
    v= float(input ('Digite um valor (ou 0 para encerrar): '))
    if v == 0:
        break
    total += v
print('Total digitado: ', total)