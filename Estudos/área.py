#Inserir as medidas do quarto
n1 = int (input ("Insira em metros, o valor da altura (Valor Inteiro): "))
n2 = int (input ("Insira em metros, o valor da base (Valor Inteiro): "))

#Loading
print ("-" * 30)
print ("Calculando Área")
print ("-" * 30)

#Guardar o valor da área
n3 = n1 * n2

#Resultado com o Projeto
print ("-" * 30)
print (f"A área do seu ambiente é: {n3}m²")
print ("-" * 30)

#Mapa do Projeto
row = n1
col = n2
 
 #Rodar pelos row's
for i in range(row):
     #Verificar se é o primeiro row ou o ultimo
    if(i==0 or i == row-1):
        print("* " * col)
    else: #Se não...
        print("*",end="") #Printar o primeiro da linha
        for j in range(col): #Rodar pelas colunas
            if j == col-1: #Verificar se é a ultima coluna
                print("") 
            elif j == col-2: #Verificar se é a penultima coluna
                print(" *",end="") #Printarum* espaço em branco
            else: #Printar dois espaços em branco
                print(" ",end=" ")

print()     