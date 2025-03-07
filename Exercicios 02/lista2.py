## Par ou Ímpar?
numero = int(input("Digite um número inteiro: "))

if numero % 2 == 0:
    print("O número é par.")
else:
    print("O número é ímpar.")


## Maior Número
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print("O maior número é:", num1)
elif num2 > num1:
    print("O maior número é:", num2)
else:
    print("Os números são iguais.")


## Classificação de Idade
idade = int(input("Digite sua idade: "))

if idade < 18:
    print("Menor de idade")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")


## Cálculo de Média e Aprovação
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
media = (nota1 + nota2) / 2

print("Média:", media)
if media >= 7:
    print("Aprovado")
elif media >= 5:
    print("Recuperação")
else:
    print("Reprovado")


## Verificação de Triângulo
lado1 = float(input("Digite o primeiro lado: "))
lado2 = float(input("Digite o segundo lado: "))
lado3 = float(input("Digite o terceiro lado: "))

if (lado1 + lado2 > lado3) and (lado1 + lado3 > lado2) and (lado2 + lado3 > lado1):
    print("Os valores formam um triângulo válido.")
else:
    print("Os valores não formam um triângulo válido.")
