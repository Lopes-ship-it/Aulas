


numeros = [1, 2, 3, 4, 5]


comprimento = len(numeros)
print("O comprimento e de:", comprimento)


#----------------------------------------------------------------------------------------


def soma(a, b):
    resultado = a + b
    return resultado

resultado_soma= soma(5, 3)
print(" A soma de 5 e 3:", resultado_soma)

#----------------------------------------------------------------------------------------

def e_par(numero): 
    if numero % 2 == 0:
     return True
    else:
     return False
    
numero = 23

if e_par(numero):
    print(f"{numero} e um numero par.")

else: 
    print(f"{numero} nao e um numero par.")
     
#--------------------------------------------------------------------------------------
notas = [7.5, 8.5, 7.0, 6,5, 8.0]


def calcular_media(notas):
    total = sum (notas)
    media = total / len(notas)
    return media


arredondar_media = lambda media: round(media, 2)

media = calcular_media(notas)
media_arredondada = arredondar_media(media)


situacao = "Aprovado" if media_arredondada >= 7 else "Reprovado"

print("As notas do estudant foram:", notas)
print("A media do estudantes foram:", media_arredondada)
print("A situacao do estudante e:", situacao)









