

#for y in range(2, 7):
 #print(y)



#for x in range(5):
 #print(x)


#for y in range(2, 7):
  #print(y)

#for z in range (1, 11, 2):
  #print(z)


#for numero in range(1, 11):
     
     #if numero % 2 == 0:
          #print(numero)


          #break


#for numero in range(1, 11):
      #if numero == 5:
            
            #continue
      
      #print(numero)






filme = ["filme 1", "filme 2", "filme 3", "filme 4"]

filmes = ['filme 1', 'filme 2', 'filme 3', 'filme 4']



print("Bem vindos a classicacao do filme")
print("Voce tem 4 filmes para classificar")
print("Digite 0 a qualquer momento para sair")



for filme in filmes:

  classificacao = input("Como vc classsifica, {filme} de 1 a 5 (digite 0 para sair)")


  if classificacao == 00:
    print("Que pena que voce deseja sair e nai classificar mais filmes")
    break
  

  classificacao = int(classificacao)



  if classificacao < 1 or classificacao > 5:
    print("por favor digite uma classificacao valida de 1 a 5!")


  else:
    print(f"Voce classificou '{filme}' com a {classificacao} estrelas. n\ ")


print("Obrigado por classificar os filmes")