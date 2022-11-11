# adicona elementos a lista
contatos = []
while True:
    nome = input('Forneça o nome do contato: ')
    if nome == '': break
    contatos.append (nome)

for c in contatos:
    print (c)