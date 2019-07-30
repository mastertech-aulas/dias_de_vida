dia = int(input('Dia do seu nascimento.\n:'))
mes = int(input('Mês do nascimento.\n:'))
ano = int(input('ano do nascimento.\n:'))

diasDeVida = ((2019-ano)*360)+(mes*30)+dia

print('Você já viveu {} dias.'.format(diasDeVida))