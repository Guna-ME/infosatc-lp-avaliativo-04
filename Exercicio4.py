#Crie uma função que receba por parâmetro DUAS palavras e verifique se uma é o inverso da outra.
def verifica(palavra):
    inversao = palavra1
    return inversao[::-1]

palavra1 = (input("Digite a primeira palavra: "))
palavra2 = (input("Digite a segunda palavra: "))
invertido = verifica(palavra1)

if palavra1 == palavra2:
    print("As palavras são iguais.")
else:
    print("As palavras são inversas ou distintas.")
