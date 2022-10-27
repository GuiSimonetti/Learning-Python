#Para receber os preços

n1 = float(input ("Digite o valor do Kg da picanha (R$0.00):"))
n2 = float(input ("Digite a quantidade em Kg da picanha:"))
n3 = int(input("Digite a quantidade de refrigerantes:"))
n4 = float(input("Digite o valor do refrigerante (R$0.00):"))

#Imprime os valores totais
print ("-" * 30)
print ("Valor Total da Picanha: ", n1 * n2)
print ("Valor Total do Refrigerante: ", n3 * n4)
print ("Valor Total dos Produtos: ", n1 * n2 + n3 * n4)
print ("-" * 30)