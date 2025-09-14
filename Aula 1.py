texto =  "Explorando a diversidade de linguagens de programcao em Python."

print(f"Tamanho do texto = {len(texto)}")
print(f"Python in texto = {'Python' in texto}")
print(f"Quantidade de e no texto = {texto.count('e')}")
print(f"As 10 primeiras letras sao: {texto[:10]}")
      




cores = ['vermelho','azul','verde','amarelo','roxo']

for cor in cores:
    print(f'Posicao = {cores.index(cor)}, cor = {cor}')





linguagens = ["Python","Java","JavaScript","C","C$","C++","Swift","Go","Kotlin"]
print("Antes da listcomp = ",linguagens)

linguagens = [item.lower() for item in linguagens]
print("\nDepoisss daa listcomp =", linguagens)



precos_em_dolares = [100, 50, 75, 120]

taxa_de_cambio = 5.25

precos_em_reais = list(map(lambda x: x * taxa_de_cambio, precos_em_dolares))

print(precos_em_reais)



numeros = [1,2,3,4,5,6,7,8,9,10]

numeros_pares = list(filter(lambda x:x %2 == 0, numeros))
print(numeros_pares)




vogais = ('a','e','i','o','u')

print(f"Tipo do objeto vogais= {type(vogais)}")

for p, x in enumerate(vogais):
     print(f"Posicao = {p}, valor = {x}")






     #exemplo lista de convidados





convidados = ("Alice", "Bob", "Carol", "David", "Eve")

confirmados = ["Bob", "David"]

nao_confirmados = [convidado for convidado in convidados if convidado not in confirmados]
print("convidados que ainda nao confirmaram:")

for pessoa in nao_confirmados:
     print(pessoa)

print("\nEnviando lembretes para os convidados que ainda nao confirmaram.")



