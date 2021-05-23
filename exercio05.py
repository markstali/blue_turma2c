#05 - Refatore o exercício 2, para que uma função receba a frase, faça todo o tratamento necessário e retorne o resultado. Depois mostre na tela o resultado e a quantidade de letras foram retiradas da frase original.
print('-='*30)
frase = input('Digite uma frase:  ')
a = e = i = o = u = 0
for vogais in frase:
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
           Tem {a} A
           Tem {e} E
           Tem {i} I
           Tem {o} O
           Tem {u} U
     ''')
print('-='*30)
quantle = a + e + i + o + u
print(f'Foram retiradas {quantle} vogais da sua frase')
for c in frase:
    if c in 'Aa' or c in 'Ee' or c in 'Ii' or c in 'Oo' or c in 'Uu' or c in" " :
        frase = frase.replace(c,' ')
print(f'A frase sem vogais = {frase}')
print('-='*30) 
