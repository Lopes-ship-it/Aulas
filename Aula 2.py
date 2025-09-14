





nome = input("Bem vindo, qual o seu nome?")
print(nome)


print((f"{nome}, Bem vindo ao cinema ******, poderia nos informar sua idade para que possamos da algumas sugestooes de filmes ?" ))


idade = int(input("Por favor, digite sua idade: "))

if idade < 14:
    print("Temos os seguintes filmes infatis para essa faixa etária de idade, " \
    "O Pequeno Principe, " \
    "Rei leao," \
    "Moana")

elif 14 <= idade < 18:
    print("Recomendamos o seguinte filmes team para essa faixa etária de idade, "
"Fast and Furios, " \
    "Vingadores," \
    "Barbie")

else: 
    print("Recomendamos o seguinte filmes adulto para essa faixa etária de idade, " \
    "Duro de matar, " \
    "missao Impossivel," \
    "Tropa de Elite")

quantidade_ingressos = 10

if quantidade_ingressos > 1:
    print(f"{nome}, os ingressos estao disponveis. Divirta-se com o filme!")

else:
    print(f"{nome}, infelizmente nao temos ingressos disponiveis!")

