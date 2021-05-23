#01 - Utilizando estruturas condicionais faça um programa que pergunte ao usuário dois números e mostre:

print('-='*30)
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
resultado = num1 + num2# A soma deles;
print('-='*30)
if resultado % 2 == 0:
   print(f'A soma de {num1} + {num2} = {resultado} que é um numero par')# Verifique se o resultado da soma é par ou impar e mostre na tela;
else:
   print(f'A soma de {num1} + {num2} = {resultado} que é um numero impar')# Verifique se o resultado da soma é par ou impar e mostre na tela;
print(f'A subtração de {num1} - {num2} = {num1-num2}')
print(f'A multiplicação de {num1} * {num2} = {num1*num2}') # A multiplicação entre eles;
print(f'A divisão de {num1} / {num2} = {num1/num2}')# A divisão inteira deles;
print('-='*30)
if num1 > num2:
   print(f'O {num1} é maior que {num2}')# Mostre na tela qual é o maior;
elif num1 < num2:
   print(f'O {num2} é maior que {num1}')# Mostre na tela qual é o maior;
else:
   print(f'{num1} e {num2} são iguais')# Mostre na tela qual é o maior;
print('-='*30)
reDiv = num1/num2
if num1 * num2 > 40:
   print(f'O resultado de {num1} * {num2} é maior que 40')
   if int(reDiv) == 0:
      print(f'{reDiv} é um numero real menor que 1 seu numero inteiro da {int(reDiv)}.NÃO DA PRA DIVIDIR POR ZERO')
   else:
      maior40 = num1* num2 / (int(reDiv))
      print(f'{num1*num2} dividido por {int(reDiv)}(resultado inteiro da divisão de {num1} / {num2}) é {maior40}')# Se a multiplicação entre eles for maior que 40, divida pelo resultado da divisão inteira e mostre o resultado na tela. Se não, mostre que a multiplicação não foi maior que 40
else:
   print(f'O resultado de {num1} * {num2} não é maior que 40')
print('-='*30)