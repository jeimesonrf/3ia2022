from alunos import Aluno, Estudante

aluno1 = Aluno('Fulano de tal','A Mãe')
print('e:',aluno1.endereco)
print('p:',aluno1.pai)
aluno1.pai = 'O Pai fujão'
print('p:',aluno1.pai)
aluno2 = Aluno('Cicrano de tal','A Mãe')
print('m2: ',aluno2.mae)
aluno1.estudar()
aluno2.estudar()

e1 = Estudante()
e1.estudar()