## Contagem Progressiva
n = int(input("Digite um número inteiro positivo: "))

# Exibe os números de 1 até n, um por linha
for i in range(1, n + 1):
    print(i)


## Soma de Números Positivos
soma = 0

while True:
    num = int(input("Digite um número (número negativo para encerrar): "))
    if num < 0:
        break  # Interrompe o loop se o número for negativo
    soma += num

print("A soma dos números positivos é:", soma)


## Tabuada de um Número
n = int(input("Digite um número inteiro: "))

print("Tabuada de", n)
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")


## Números Ímpares em um Intervalo
a = int(input("Digite o primeiro número do intervalo: "))
b = int(input("Digite o segundo número do intervalo: "))

# Define o menor e o maior número para o intervalo
inicio = min(a, b)
fim = max(a, b)

print("Números ímpares no intervalo de", inicio, "a", fim, ":")

# Percorre o intervalo e exibe os números ímpares
for num in range(inicio, fim + 1):
    if num % 2 != 0:
        print(num)


## Sequência de Fibonacci
n = int(input("Quantos termos da sequência de Fibonacci deseja exibir? "))

a, b = 0, 1

if n >= 1:
    print(a, end=" ")
if n >= 2:
    print(b, end=" ")

# Calcula e exibe os termos restantes da sequência
for i in range(3, n + 1):
    c = a + b
    print(c, end=" ")
    a, b = b, c  # Atualiza os valores para o próximo termo

