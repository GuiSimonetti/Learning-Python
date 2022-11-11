# adiciona apenas itens exclusivos na lista
lista = ['maionese', 'ervilha', 'carne', 'tomate']
produto = input ("Nome do produto?: ")
if produto in lista:
    print ('Produto já existente na lista!')
else:
    lista.append (produto)
    print ('Produto adicionado a lista! ')

    print ('Lista atual de produtos: ')
    for p in lista:
        print (p)