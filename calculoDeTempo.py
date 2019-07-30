from datetime import date

data_atual = date.today()

dia = int(input('Dia do seu nascimento.\n:'))
mes = int(input('Mês do nascimento.\n:'))
ano = int(input('ano do nascimento.\n:'))

diasDeVida = 0

for x in range(ano+1, data_atual.year):
    if x % 4 == 0:
        #ano bissexto
       diasDeVida += 366
    else:
        diasDeVida += 365

diasDeVida += ((12-mes) + (data_atual.month-1))*30+data_atual.day

print('Você já viveu {} dias.'.format(diasDeVida))