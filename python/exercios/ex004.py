from this import d


digitado= input('digite algo ')
print(type(digitado))
print('Você digitou um numero ',digitado.isnumeric())
print('você digitou uma letra/palavra ', digitado.isalpha())
print('você digitou  palavra e numero ', digitado.isalnum())
print('Você digitou em maiusculo ', digitado.isupper())
print('você digitou em minusculo', digitado.islower())
print('você digitou em maiuscolo e minusculo  ', digitado.istitle())
print('você digitou espaço ', digitado.isspace())
