
## 1.Divisão Segura
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira números válidos.")
else:
    print("Resultado da divisão:", resultado)


## 2.Abertura Segura de Arquivo
nome_arquivo = input("Digite o nome do arquivo a ser lido: ")
try:
    with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
        conteudo = arquivo.read()
        print("Conteúdo do arquivo:")
        print(conteudo)
except FileNotFoundError:
    print("Erro: Arquivo não encontrado.")
except Exception as e:
    print("Erro ao abrir o arquivo:", e)


## 3.Conversão de Entrada com Exceções
while True:
    entrada = input("Digite um número inteiro: ")
    try:
        numero = int(entrada)
        print("O dobro de", numero, "é", numero * 2)
        break  # Sai do loop se a conversão for bem-sucedida
    except ValueError:
        print("Erro: Entrada inválida. Por favor, tente novamente.")


## 4.Acesso a Elementos de uma Lista
lista = [10, 20, 30, 40, 50]
entrada = input("Digite um índice entre 0 e 4 para acessar um valor da lista: ")
try:
    indice = int(entrada)
    valor = lista[indice]
    print("Valor no índice", indice, "é", valor)
except IndexError:
    print("Erro: Índice inválido. Escolha um valor entre 0 e 4.")
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira um número inteiro.")


## 5.Operações Bancárias com Tratamento de Erros
class SaldoInsuficiente(Exception):
    pass
saldo = 1000.0
try:
    valor_saque = float(input("Digite o valor do saque: R$ "))
    if valor_saque > saldo:
        raise SaldoInsuficiente("Saldo insuficiente para realizar o saque.")
    saldo -= valor_saque
    print("Saque realizado com sucesso. Saldo atual: R$ {:.2f}".format(saldo))
except ValueError:
    print("Erro: Entrada inválida. Por favor, insira um valor numérico.")
except SaldoInsuficiente as e:
    print("Erro:", e)

