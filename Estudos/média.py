#Insira o valor de cada nota (Todas as provas possuem o mesmo peso)

nome = input ("Insira o nome do Aluno: ")
print ("Todos os valores das provam devem ser no formato: 0.00")
n1 = float (input ("Insira o valor da Prova 1: "))
n2 = float (input ("Insira o valor da Prova 2: "))
n3 = float (input ("Insira o valor da Prova 3: "))
n4 = (n1+n2+n3) /3
#Separador
print ("-" * 30)
#Resulto matemático 
print("A média de " +nome+ " foi", n4)
#Separador
print ("-" * 30)