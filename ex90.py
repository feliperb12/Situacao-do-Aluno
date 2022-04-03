
       
aluno= dict()
aluno['nome']=str(input('Nome: '))
aluno['Média']=float(input(f'Média de {aluno["nome"]}: '))
if aluno['Média'] >=7:
    aluno['situaçao']='Aprovado'
elif 5<=aluno['Média'] <7:
        aluno['situação']='Recuperação'
else:
    aluno['situação']='Reprovado'
    
print('-*-'*20)

for k,v in aluno.items():
    print(f'{k} é igual a {v}')