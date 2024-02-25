#Permitem o desvio de fluxo de controle, quando determinadas expressoes logicas sao atendidas 


MOIOR_IDADE = 18
IDADE_ESPECIAL = 12

idade = int(input("Infome sua idade:"))

if idade >= MOIOR_IDADE:
    print("Maior de Idade Pode Tirar a CNH")

if idade < MOIOR_IDADE:
    print("Ainda não pode tirar a CNH")


if idade >= MOIOR_IDADE:
    print("MAior de idade pode tirar a CNH")
else:
    print("Ainda não pode tirar a CNH")    


if idade >= MOIOR_IDADE:
    print("Maior de idade pode tirar a CNH")
elif idade == IDADE_ESPECIAL:
    print("pode fazer aulas teóricas, mas não pode fazer aulas práticas.")
else:
    print("Ainda não pode tirar a CNH")    