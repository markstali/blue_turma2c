#04 - Utilizando funções e listas faça um programa que receba uma data no formato DD/MM/AAAA e devolva uma string no formato DD de mesPorExtenso de AAAA. Opcional: valide a data e retorne 'data inválida' caso a data seja inválida.

def data(): 
   datalis = []
   print('Data atual: ')
   dd = int(input('Dia: '))
   datalis.append(dd)
   if dd < 1 or dd> 31:
      print('Dia invalido')
   mm = int(input('Mes: '))
   datalis.append(mm)
   aaa = int(input('Ano: '))
   datalis.append(aaa)
   print(datalis)
   if aaa < 1900 or aaa < 2021:
      print('Ano invalido!')
   if mm == 1:
      print(f'{dd} Janeiro {aaa}')
   elif mm == 2:
      print(f'{dd} Fevereiro {aaa}')
   elif mm == 3:
      print(f'{dd} Março {aaa}')
   elif mm == 4:
      print(f'{dd} Abril {aaa}')
   elif mm == 5:
      print(f'{dd} Maio {aaa}')
   elif mm == 6:
      print(f'{dd} Junho {aaa}')
   elif mm == 7:
      print(f'{dd} Julho {aaa}')
   elif mm == 8:
      print(f'{dd} Agosto {aaa}')
   elif mm == 9:
      print(f'{dd} Setembro {aaa}')
   elif mm == 10:
      print(f'{dd} Outubro {aaa}')
   elif mm == 11:
      print(f'{dd} Novembro {aaa}')
   elif mm == 12:
      print(f'{dd} Dezembro {aaa}')
   else:
      print('Mês Invalido')
 
data()