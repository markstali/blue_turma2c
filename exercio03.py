#03 - Utilizando estruturas de repetição com teste lógico, faça um programa que peça uma senha para iniciar seu processamento, só deixe o usuário continuar se a senha estiver correta, após entrar dê boas vindas a seu usuário e apresente a ele o jogo da advinhação, onde o computador vai “pensar” em um número entre 0 e 10. O jogador vai tentar adivinhar qual número foi escolhido até acertar, a cada palpite do usuário diga a ele se o número escolhido pelo computador é maior ou menor ao que ele palpitou, no final mostre quantos palpites foram necessários para vencer.

from random import randrange, vonmisesvariate
print('-='*30)
user = str(input("Digite a Senha: "))
senha = 'blue'
while user != senha:
   print('-='*30)
   print('Dica de senha: Melhor escola de tecnologia')
   print('-='*30)
   user = str(input("Digite a senha novamente: "))
print('   Bem vindo(a)\n   Vamos brincar!')
print('-='*30)
print('''
   Esse é o jogo da adivinhação.
   O computador vai pensar um numero
   e vc tem que adivinhar qual foi!
      ''')
print('-='*30)
print(("Qual o numero que o computador pensou?: "))
numSort = randrange(12)
n = -1
c = 0
t = 1
while n != numSort:
   n = int(input(f"{t}ª tentativa: "))
   if n > numSort:
      print('O computador pensou em numero MENOR!')
   elif n == numSort:
      print('-='*30)
      print(' '*8,'=Acertou!=')
   else:
      print('O computador pensou em numero MAIOR')
   c += 1
   t += 1
print(f'''
   O computador pensou em {numSort}
   Parabens acertou com {c} tentativas
      ''')
print('-='*30)