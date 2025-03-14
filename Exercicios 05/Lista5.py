
## Cálculo do Fatorial
def calcular_fatorial(n):
    if n < 0:
        return None
    resultado = 1
    for i in range(1, n + 1):
        resultado *= i
    return resultado

numero = int(input("Digite um número para calcular o fatorial: "))
print(f"O fatorial de {numero} é {calcular_fatorial(numero)}")


## Verificação de Número Primo
def eh_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Digite um número para verificar se é primo: "))
print(f"{numero} é primo?" , "Sim" if eh_primo(numero) else "Não")

## Cálculo da Média de uma Lista
def calcular_media(lista):
    if not lista:
        return 0
    return sum(lista) / len(lista)

entrada = input("Digite números separados por espaço: ")
numeros = list(map(float, entrada.split()))
print(f"Média: {calcular_media(numeros):.2f}")

## Contador de Vogais em uma Palavra
def contar_vogais(palavra):
    vogais = {'a', 'e', 'i', 'o', 'u'}
    return sum(1 for letra in palavra.lower() if letra in vogais)

palavra = input("Digite uma palavra: ")
print(f"Número de vogais: {contar_vogais(palavra)}")


## Conversão de Temperatura
def celsius_para_fahrenheit(celsius):
    return (celsius * 9/5) + 32

c = float(input("Digite a temperatura em Celsius: "))
print(f"{c}°C equivalem a {celsius_para_fahrenheit(c):.1f}°F")