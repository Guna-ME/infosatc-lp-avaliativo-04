#No exercício da última semana, de desenvolver um sistema para verificar se a pessoa está apta
#  para doação de sangue, você criou todo o sistema sem utilizar funções.
#  Nessa nova versão mantenha os recursos e verificações que foram propostas, 
#  porém, separe em funções as validações e recursos.
#  Exemplo: função para fazer a validação se a pessoa está apta: def validaRequisitos():
#  onde dentro do escopo da função, você deve colocar o processo de validação e retornar true ou false
#  para mostrar ao usuário se ele está apto ou não.

nome=[]
cpf=[]
senha=[]
aptidao=[]

def printFinal():
    print("Nome:   ",nome," \nCPF:    ",cpf," \nSenha:  ",senha," \nAptidão:",aptidao)
def cadastroDados():
    nome.append(input("Insira seu nome:"))
    cpf.append(input("Insira seu cpf:"))
    senha.append(input("Insira sua senha:"))
    aptidao.append(input("Insira aqui se você está apto para doação de sangue:"))
    printFinal()

idade=(int(input("Insira a sua idade: ")))
peso=(float(input("Insira o seu peso: ")))
horas=(int(input("Insira quantas horas dormiu na noite passada: ")))

if idade>=16 and idade<=69:
    idade+=1
else:
    print("Idade fora dos requisitos!")
if peso>50:
    peso+=1
else:
    print("Peso fora dos requisitos!")
if horas>=6:
    horas+=1
else:
    print("Horas de sono fora dos requisitos!")
if idade == 1 and peso == 1 and horas == 1:
    print("Você pode ser um doador!")
    cadastro = (input("Parabéns! Você pode ser um doador, deseja se cadastrar? Digite 1-Sim ou 2-Não:"))
    if cadastro=="2":
        pessoaCadastrada = pessoaCadastrada+1
        cadastroDados()
    else:
        print("Cadastro negado.")
