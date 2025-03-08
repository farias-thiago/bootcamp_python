# Operações com Inteiros (`int`)

## 1. Soma de dois números inteiros

```python
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
resultado_soma = num1 + num2
print("A soma é: ", resultado_soma)
```
## 2. Resto da divisão por 5

```python
num = int(input("Digite um número: "))
resultado_resto = num % 5
print("O resto da divisão por 5 é: ", resultado_resto)
```

## 3. Multiplicação de dois números
```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado_multiplicacao = num1 * num2
print("O resultado da multiplicação é: ", resultado_multiplicacao)
```

## 4. Divisão inteira de dois números
```python
num1 = int(input("Digite o primeiro número inteiro: "))
num2 = int(input("Digite o segundo número inteiro: "))
resultado_divisao_inteira = num1 // num2
print("O resultado da divisão inteira é: ", resultado_divisao_inteira)
```

## 5. Quadrado de um número
```python
num = int(input("Digite um número: "))
resultado_quadrado = num ** 2
print("O quadrado do número é: ", resultado_quadrado)
```

---
# Números de Ponto Flutuante (`float`)

## 6. Escreva um programa que receba dois números flutuantes e realize sua adição.
```python
num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
resultado_soma = num1 + num2
print("A soma é: ", resultado_soma)
```
## 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.
```python
num1 = float(input("Digite o primeiro número flutuante: "))
num2 = float(input("Digite o segundo número flutuante: "))
media = (num1 + num2) / 2
print("A média é: ", media)
```
## 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).
```python
base = float(input("Digite a base: "))
expoente = float(input("Digite o expoente: "))
potencia = base ** expoente
print("O resultado da potência é: ", potencia)
```
## 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.
```python
celsius = float(input("Digite a temperatura em Celsius: "))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius}°C é igual a {fahrenheit}°F")
```
## 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.
```python
from math import pi
raio = float(input("Digite o raio do círculo: "))
area = pi * raio ** 2
print("A área do círculo é: ", area)
```
---
# Strings (`str`)

## 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.
```python
texto = input("Digite um texto: ")
texto_maiusculas = texto.upper()
print("Texto em maiúsculas: ", texto_maiusculas)
```
## 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.
```python
nome_completo = input("Digite seu nome completo: ")
nome_minusculas = nome_completo.lower()
print("Nome em minúsculas: ", nome_minusculas)
```
## 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.
```python
frase = input("Digite uma frase: ")
frase_sem_espacos = frase.strip()
print("Frase sem espaços no início e no final: ", frase_sem_espacos)
```
## 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.
```python
data = input("Digite uma data no formato dd/mm/aaaa: ")
dia, mes, ano = data.split("/")
print("Dia:", dia)
print("Mês:", mes)
print("Ano:", ano)
```
## 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.
```python
parte1 = input("Digite a primeira parte do texto: ")
parte2 = input("Digite a segunda parte do texto: ")
texto_concatenado = parte1 + parte2
print("Texto concatenado: ", texto_concatenado)
```
---
# Booleanos (`bool`)

## 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.
```python
valor1 = True
valor2 = False
resultado_and = valor1 and valor2
print("Resultado do AND lógico:", resultado_and)
```
## 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
```python
resultado_or = valor1 or valor2
print("Resultado do OR lógico:", resultado_or)
```
## 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
```python
resultado_not = not valor1
print("Resultado do NOT lógico:", resultado_not)
```
## 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.
```python
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))
resultado_igualdade = (num1 == num2)
print("Resultado da igualdade:", resultado_igualdade)
```
## 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.
```python
resultado_diferenca = (num1 != num2)
print("Resultado da diferença:", resultado_diferenca)
```