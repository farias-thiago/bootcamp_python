# 🚀 Código Python Básico

Este código contém exemplos simples em Python, incluindo um desafio prático. Abaixo está o código comentado e organizado para facilitar o entendimento.

---

## 📌 Exemplo 1: Hello World e Soma de Números

```python
# Imprime "Hello World" no console
print("Hello World")

# Solicita dois números ao usuário e calcula a soma
num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
print(f"A soma dos números é: {num1 + num2}")

```
---
## 🎯 Desafio: Cálculo de Salário com Bônus

Neste desafio, o programa solicita o nome do usuário, seu salário e um bônus. Em seguida, calcula o salário total, incluindo um bônus constante.

```python
# Constante que representa um bônus fixo
CONSTANTE_BONUS = 1000

# Solicita o nome do usuário
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")  # Saída personalizada com o nome

# Solicita o salário e o bônus do usuário
salario = float(input("Digite seu salário: "))
bonus = float(input("Digite o valor do bônus: "))

# Calcula e exibe o salário total (salário + bônus + bônus constante)
print(f"O salário total é: {salario + bonus + CONSTANTE_BONUS}")
```