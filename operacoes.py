# Sorteando número e pedindo ao usuário


import random as sorteandoNumeros
# Acima renomeando a biblioteca

aleatorio1=sorteandoNumeros.randint(1,10)
aleatorio2=sorteandoNumeros.randint(1,20)

print('O número sorteado é: ', aleatorio1)
print('O outro número sorteado é: ', aleatorio2)

soma=aleatorio1+aleatorio2

while True:
  resultadoSoma=int(input('Qual a soma dos números? '))
  if resultadoSoma==soma:
    print('Parabéns, você acertou!')
    break
  else:
    print('Você errou')

multiplicacao=aleatorio1*aleatorio2

while True:
  resultadoMultiplicacao=int(input('Qual a multiplicação? '))
  if resultadoMultiplicacao==multiplicacao:
    print('Parabéns, acertou novamente!')
    break
  else:
    print('Você errou, tente novamente')

subtracao=aleatorio1-aleatorio2

while True:
    resultadoSubtracao=int(input('Qual a subtração? '))
    if resultadoSubtracao==subtracao:
        print('Parabéns, acertou mais uma vez!')
        break
    else:
        print('Errou')
        
divisao=aleatorio1/aleatorio2

while True:
    resultadoDivisao=float(input('Qual a divisão? '))
    if resultadoDivisao==divisao:
        print('Parabéns, você é um gênio!')
        break
    else:
        print('Tente novamente.')
