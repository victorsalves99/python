nome=input('digite o nome do aluno? ' )
nota1=float(input('digite  nota um ? '))
nota2=float(input('digite a nota dois? '))
notafinal=float(nota1+nota2)
media=float(notafinal/2)
if media>=6:
    resultado=('aprovado')
else:
    resultado=('reprovado')

print('o aluno(a){}, tem na nota um {:.1f} ,na nota dois {:.1f} ,tendo a nota final {:.1f} e a media de {} por tanto esse aluno(a)foi {}'.format(nome,nota1,nota2,notafinal,media,resultado))

