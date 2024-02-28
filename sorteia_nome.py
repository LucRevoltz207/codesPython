import random

nome1 = (input("nome do primeiro aluno: "))
nome2 = (input("nome do segundo aluno: "))
nome3 = (input("nome do terceiro aluno: "))
nome4 = (input("nome do quarto aluno: "))

sort = random.choice([nome1,nome2,nome3,nome4])
print("O aluno sorteado foi: {}".format(sort))