row = 4
col = 8
 
 #rodar pelos row's
for i in range(row):
     #Verificar se é o primeiro row ou o ultimo
    if(i==0 or i == row-1):
        print("* " * col)
    else: #se não...
        print("",end="") #Printar o primeiro da linha
        for j in range(col): #Rodar pelas colunas
            if j == col-1: #Verificar se é a ultima coluna
                print("") 
            elif j == col-2: #Verificar se é a penultima coluna
                print(" ",end="") #Printarum* espaço em branco
            else: #printar dois espaços em branco
                print(" ",end=" ")

print()