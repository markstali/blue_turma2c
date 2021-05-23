#02 - Utilizando estruturas de repetição com variável de controle, faça um programa que receba uma string com uma frase informada pelo usuário e conte quantas vezes aparece as vogais a,e,i,o,u e mostre na tela, depois mostre na tela essa mesma frase sem nenhuma vogal.

print('-='*30)
palavra = str(input('Digite uma palavra com 8 digitos(espaços contam!):  '))
while len(palavra) > 8:
   print('Você digitou mais que 8 digitos!')
   palavra = str(input('Digite uma palavra com 8 digitos(espaços contam!):  '))
a = e = i = o = u = 0
for vogais in palavra:
    if vogais in 'Aa':
        a+=1
    if vogais in 'Ee':
        e+=1
    if vogais in 'Ii':
        i+=1
    if vogais in 'Oo':
        o+=1
    if vogais in 'Uu':
        u+=1
print(f''' 
           Tem {a} A:
           Tem {e} E
           Tem {i} I
           Tem {o} O
           Tem {u} U
     ''')
print('-='*30)
for c in palavra:
    if c in 'Aa' or c in 'Ee' or c in 'Ii' or c in 'Oo' or c in 'Uu' or c in" " :
        palavra = palavra.replace(c,' ')
print(f'A frase sem vogais = {palavra}')
print('-='*30)
