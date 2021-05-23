#08 - Crie um programa que leia nome, ano de nascimento e carteira de trabalho e cadastre-os (com idade) em um dicionário. Se por acaso a CTPS for diferente de 0, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente , além da idade, com quantos anos a pessoa vai se aposentar. Considere que o trabalhador deve contribuir por 35 anos para se aposentar.
from datetime import datetime
print('-='*30)
dados = {}
dados['Nome'] = str(input("Nome: ")).upper()[0]
dados['AnoNasc']= int(input("Ano Nascimento: "))
dados['Idade'] = datetime.now().year - dados['AnoNasc']
if dados['Idade'] < 65:
    dados['TempoAposen'] = dados['Idade'] - 65
else:
    dados['TempoAposen'] = 'Voce deve ser apsentado!'
print('    "Se não tem CTPS digite [0]Zero"')
dados['CTPS'] = int(input("Nº CTPS: "))
if dados['CTPS'] != 0:
    dados['Ano1Contr'] = int(input("Ano primeira Constração: "))
    dados['SalarioAtu'] = float(input("Salario atual: "))
    if dados['Idade'] < 65:
        dados['TempoAposen'] = 35 - (datetime.now().year - dados['Ano1Contr'])
    else:
        dados['TempoAposen'] = 'Voce deve ser apsentado!'
print('-='*30)
for k,v in dados.items():
    print(f'{k} : {v}')
print('-='*30)