#criação e leitura de listas
sudeste = ['São Paulo', 'Minas Gerais', 'Rio de Janeiro', 'Espirito Santo']
notas = [5.4, 7.5, 8.6, 10]
qtde_estados_sudeste = len (sudeste);

print ('Estados do Sudeste: ')
for n in range (qtde_estados_sudeste):
    print (n+1, sudeste[n])
print ('-' * 30)

print ('Notas: ')
for n in notas:
    print (n)