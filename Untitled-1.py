print ("hello wolrd!")


x = 10
nome = 'aluno'
nota = 8.75
fez_inscricao = True


print(type(x))
print(type(nome))
print(type(nota))
print(type(fez_inscricao))



nome = input("Digite um nome:")
print(nome)



print("Ola, %s, bem-vindo a disciplina de programacao. Parabens pelo seu primeiro Hello world" %(nome))

print(f"{nome}, bem vindo a disciplina de programacao. Parabens pelo seu primeiro Hello World")


Nota_1=int(input("Digite a primeira nota:"))
Nota_2=int(input("Digite a segunda nota:"))
Nota_3=int(input("Digite a terceira nota:"))
Nota_4=int(input("Digite a quarta nota:"))

media = (Nota_1+Nota_2+Nota_3+Nota_4) /4


if media >= 6:
  situacao = "aprovado"
else:
   situacao = "reprovado"

print(f"A media das notas {media: .1f}")

print(f"A situacao aluno e {situacao}")
