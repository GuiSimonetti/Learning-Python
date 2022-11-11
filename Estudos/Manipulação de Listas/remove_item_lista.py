# remove item da lista 

#Apresenta os itens da lista
pendencias = ['exercitar', 'estudar', 'limpar', 'escovar', 'beber']
print ('Relação de pendências: ', pendencias)
print ('_' * 80)
#remove os itens da lista
item = input ('Digite a pendência a remover: ')
pendencias.remove (item)
print ('Pendências atuais: ', pendencias)