import math


## Cálculo da Área do Círculo
raio = float(input("Digite o valor do raio do círculo: "))
area = math.pi * (raio ** 2)
print("A área do círculo é:", area)


## Conversão de Temperatura
celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print("A temperatura em Fahrenheit é:", fahrenheit)


## Média de Três Números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

media = (num1 + num2 + num3) / 3
print("A média dos três números é:", media)


## Cálculo do Salário Mensal
horas_trabalhadas = float(input("Digite o número de horas trabalhadas no mês: "))
valor_por_hora = float(input("Digite o valor recebido por hora: "))

salario = horas_trabalhadas * valor_por_hora
print("O salário total do mês é:", salario)


## Conversão de Medidas – Metros para Centímetros
metros = float(input("Digite um valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros equivalem a {centimetros} centímetros.")

