#Crie uma função que receba uma palavra por parâmetro e permita inverter a ordem dessa palavra.
def inversao(palavra):
    inversao = palavra
    return inversao[::-1]

palavra = (input("Palavra desejada para inversão: "))
invertido = inversao(palavra)
print("A palavra invertida: ", invertido)
