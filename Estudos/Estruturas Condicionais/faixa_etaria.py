#Faixa etária de acordo com a idade
idade = int(input ("Digite sua idade: "))

if (idade < 0):
    print ("Você realmente está vivo?")
elif (idade >= 0 and idade <= 3) :
    print ("Você é um bebê")
elif (idade >= 4 and idade <=12) :
    print ("Você é uma criança")
elif (idade >= 13 and idade <=17) :
    print("Você é uma adolescente")
elif (idade >=18 and idade <=59) :
    print ("Você é um adulto")
else:
    print ("Você já não é tão novo assim")
