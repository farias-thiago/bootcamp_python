#######################
#Exemplos Práticos
#######################


import csv

# Caminho para o arquivo CSV
caminho_arquivo = 'exemplo.csv'

# Inicializa uma lista vazia para armazenar os dados
dados = []

# Usa o gerenciador de contexto `with` para abrir o arquivo
with open(caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    # Cria um objeto leitor de CSV
    leitor_csv = csv.DictReader(arquivo)
    
    # Itera sobre as linhas do arquivo CSV
    for linha in leitor_csv:
        # Adiciona cada linha (um dicionário) à lista de dados
        dados.append(linha)

# Exibe os dados lidos do arquivo CSV
for registro in dados:
    print(registro)


# FUNÇÃO DE ORDENAÇÃO DE LISTA

lista = [64, 34, 25, 12, 22, 11, 90]

def ordernar_lista(lista: list) -> list:
    lista_ordenada = lista.copy()

    for i in range(len(lista)):
        for j in range(i+1, len(lista)):
            if lista[i] > lista[j]:
                lista[i], lista[j] = lista[j], lista[i]

    return lista_ordenada

print(lista)




##################################
# Exercícios
##################################


# 1- Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.
numeros = list(range(1, 11))
for numero in numeros:
    print(quadrados**2)

# 2- Dada a lista ["Python", "Java", "C++", "JavaScript"], remova o item "C++" e adicione "Ruby".
linguagens = ["Python", "Java", "C++", "JavaScript"]
linguagens.remove("C++")
linguagens.append("Ruby")
print(linguagens)

# 3- Crie um dicionário para armazenar informações de um livro, incluindo título, autor e ano de publicação. Imprima cada informação.
livro = {"titulo": "1984", "autor": "George Orwell", "ano": 1949}
for chave, valor in livro.items():
    print(f"{chave}: {valor}")

# 4- Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.
def contar_caracteres(s):
    contagem = {}
    for caractere in s:
        contagem[caractere] = contagem.get(caractere, 0) + 1
    return contagem

print(contar_caracteres("engenharia de dados"))

# 5- Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.
lista_compras = ["maçã", "banana", "cereja"]
precos = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}
total = sum(precos[item] for item in lista_compras)
print(f"Preço total: {total}")

# 6. Eliminação de Duplicatas
emails = ["user@example.com", "admin@example.com", "user@example.com", "manager@example.com"]
emails_unicos = list(set(emails))

print(emails_unicos)

# 7. Filtragem de Dados. Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.
idades = [22, 15, 30, 17, 18]
idades_validas = [idade for idade in idades if idade >= 18]

print(idades_validas)

# 8. Ordenação Personalizada. Objetivo: Dada uma lista de dicionários representando pessoas, ordená-las pelo nome.
pessoas = [
    {"nome": "Alice", "idade": 30},
    {"nome": "Bob", "idade": 25},
    {"nome": "Carol", "idade": 20}
]
pessoas.sort(key=lambda pessoa: pessoa["nome"])

print(pessoas)

# 9. Agregação de Dados. Dado um conjunto de números, calcular a média.
numeros = [10, 20, 30, 40, 50]
media = sum(numeros) / len(numeros)

print("Média:", media)

# 10. Divisão de Dados em Grupos. Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.
valores = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [valor for valor in valores if valor % 2 == 0]
impares = [valor for valor in valores if valor % 2 != 0]

print("Pares:", pares)
print("Ímpares:", impares)


##################################
# EXercícios com Dicionários
##################################

# 11. Atualização de Dados. Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.
produtos = [
    {"id": 1, "nome": "Teclado", "preço": 100},
    {"id": 2, "nome": "Mouse", "preço": 80},
    {"id": 3, "nome": "Monitor", "preço": 300}
]

# Atualizar o preço do produto com id 2 para 90
for produto in produtos:
    if produto["id"] == 2:
        produto["preço"] = 90

print(produtos)

# 12. Fusão de Dicionários. Objetivo: Dados dois dicionários, fundi-los em um único dicionário
dicionario1 = {"a": 1, "b": 2}
dicionario2 = {"c": 3, "d": 4}

dicionario_fundido = {**dicionario1, **dicionario2}

print(dicionario_fundido)

# 13. Filtragem de Dados em Dicionário. Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.
estoque = {"Teclado": 10, "Mouse": 0, "Monitor": 3, "CPU": 0}

estoque_positivo = {produto: quantidade for produto, quantidade in estoque.items() if quantidade > 0}

print(estoque_positivo)

# 14. Extração de Chaves e Valores. Dado um dicionário, criar listas separadas para suas chaves e valores.
dicionario = {"a": 1, "b": 2, "c": 3}
chaves = list(dicionario.keys())
valores = list(dicionario.values())

print("Chaves:", chaves)
print("Valores:", valores)

# 15. Contagem de Frequência de Itens. Dada uma string, contar a frequência de cada caractere usando um dicionário.
texto = "engenharia de dados"
frequencia = {}

for caractere in texto:
    if caractere in frequencia:
        frequencia[caractere] += 1
    else:
        frequencia[caractere] = 1

print(frequencia)


# 16. Escreva uma função que receba uma lista de números e retorne a soma de todos os números.
def soma_lista(numeros: list) -> int:
    return sum(numeros)

lista = [1, 2, 3, 4, 5]
print(soma_lista(lista))

# 17. Crie uma função que receba um número como argumento e retorne True se o número for primo e False caso contrário.
def primo(numero: int) -> bool:
    if numero <= 1:
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False
    return True

print(primo(7))  # Saída: True
print(primo(10))  # Saída: False

# 18. Desenvolva uma função que receba uma string como argumento e retorne essa string revertida.
def reverter_string(s: str) -> str:
    return s[::-1]

print(reverter_string("Python"))  # Saída: "nohtyP"

# 19. Implemente uma função que receba dois argumentos: uma lista de números e um número. A função deve retornar todas as combinações de pares na lista que somem ao número dado.
def encontrar_pares_soma(numeros: list, soma: int) -> list:
    pares = []
    for i in range(len(numeros)):
        for j in range(i + 1, len(numeros)):
            if numeros[i] + numeros[j] == soma:
                pares.append((numeros[i], numeros[j]))
    return pares

lista = [1, 2, 3, 4, 5]
print(encontrar_pares_soma(lista, 5))  # Saída: [(1, 4), (2, 3)]

# 20. Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas
def chaves_ordenadas(dicionario: dict) -> list:
    return sorted(dicionario.keys())

dicionario = {"b": 2, "a": 1, "c": 3}
print(chaves_ordenadas(dicionario))  # Saída: ['a', 'b', 'c']
