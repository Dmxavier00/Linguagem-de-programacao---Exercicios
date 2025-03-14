
## Soma dos Elementos de uma Lista
entrada = input("Digite números inteiros separados por espaço: ")
numeros = list(map(int, entrada.split()))

soma = sum(numeros)
print("A soma dos elementos é:", soma)


## Encontrar o Maior e o Menor Número
entrada = input("Digite números separados por espaço: ")
numeros = list(map(int, entrada.split()))

maior = max(numeros)
menor = min(numeros)
print(f"Maior: {maior}, Menor: {menor}")


## Remover Duplicatas
entrada = input("Digite números separados por espaço: ")
numeros = list(map(int, entrada.split()))

vistos = set()
lista_sem_duplicatas = []
for num in numeros:
    if num not in vistos:
        lista_sem_duplicatas.append(num)
        vistos.add(num)

print("Lista sem duplicatas:", lista_sem_duplicatas)


## Inverter a Lista
entrada = input("Digite palavras separadas por espaço: ")
palavras = entrada.split()

lista_invertida = palavras[::-1]
print("Lista invertida:", lista_invertida)


## Contar Ocorrências de um Elemento
entrada_lista = input("Digite números separados por espaço: ")
numeros = list(map(int, entrada_lista.split()))

numero = int(input("Digite o número para contar: "))

ocorrencias = numeros.count(numero)
print(f"O número {numero} aparece {ocorrencias} vezes.")

