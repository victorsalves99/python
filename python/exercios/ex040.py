nome=str(input('qual o nome do aluno ? '))
nota1=float(input('nota 1 '))
nota2=float(input('nota 2 '))
media= (nota1+nota2)/2


if media < 5:

    print('sua media do aluno {} foi {} voce foi \033[1;31;43mREPROVADO! \033[m'.format(nome,media))
elif media>=7:
    print('sua media do aluno {} foi {} voce foi \033[1;32;47m APROVADO!\033[m'.format(nome,media))
else :
    print('sua media do aluno {} foi {} voce foi pra\033[1;34;43m RECUPERAÇÃO !\033[m'.format(nome,media))