#07 - Crie um programa onde o usuário possa digitar sete valores numéricos e cadastre-os em uma lista única que mantenha separados os valores pares e ímpares. No final, mostre os valores pares e ímpares em ordem crescente.
print('-='*30) 
print('      *Digite 7 numeros* ')
print('-='*30) 
pares = []
impares = []
numCrescent = []
for i in range(7):
   num = int(input('Digite un numero: '))
   numCrescent.append(num)
   if num % 2 == 0:
      pares.append(num)
   else:
      impares.append(num)
print('-='*30)  
numCrescent.sort()
pares.sort()
impares.sort()      
print('Numeros pares: ',pares)    
print('Numeros impares: ',impares)  
print('-='*30)  
print('Numeros ordem crescente:', numCrescent)
numCrescent.sort(reverse=True)
print('Numeros ordem decrescente:', numCrescent)
print('-='*30)