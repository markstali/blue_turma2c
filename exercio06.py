#06 - Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
   # "Telefonou para a vítima?"
   # "Esteve no local do crime?"
   # "Mora perto da vítima?"
   # "Devia para a vítima?"
   # "Já trabalhou com a vítima?" 
# O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
   # Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita",
   # Entre 3 e 4 como "Cúmplice" e 5 como "Assassino". 
   # Caso contrário, ele será classificado como "Inocente".

quest = []
print('-='*30)
print('''
      Você foi acusado de um crime, responda o questionario!
      Responda 1 para Sim e 0 para Não\n
      ''')
print('-='*30)


quest.append(int(input("Telefonou para a vítima?[1/0]: ")))
quest.append(int(input("Esteve no local do crime?[1/0]: ")))
quest.append(int(input("Mora perto da vítima?[1/0]: ")))
quest.append(int(input("Devia para a vítima?[1/0]: ")))
quest.append(int(input("Já trabalhou com a vítima?[1/0]: ")))
print('-='*30)

if sum(quest) == 2:
    print(' '*8,'Você foi acusado de Suspeito!')
elif sum(quest) == 3 or sum(quest) == 4:
    print(' '*8,'Você foi acusado de Cumplice!')
elif sum(quest) == 5:
    print(' '*8,'Você foi acusado de Assassino!')
elif sum(quest) > 5 or sum(quest) < 0 :
   print(' '*8,'Você respondeu alem de 0 ou 1')
else:
    print(' '*8,'Você foi acusado de Inocente!')  
print('-='*30)