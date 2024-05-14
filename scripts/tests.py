correto = 1
respostas = "1 2 3 2 1"

respostas = respostas.split(" ")

acertos = 0

for resultado in respostas:
    if int(resultado) == correto:
        acertos += 1

print(acertos)