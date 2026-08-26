import random 
import hashlib 
 
def gerarId (): 
    return f"{random.randint(1, 9999):04d}" 
 
def cript(senha): 
    return hashlib.sha256(senha.encode()).hexdigest() 
 
estudandes_db = [] 

sistema = True

while sistema:

    print('\n1. Adicionar novo aluno') 
    print('2. Excluir aluno') 
    print('3. Listar alunos')
    print('4. Sair')
 
    escolha = int(input('Selecione uma opção: ')) 
 
    if (escolha == 1): 
        adicionarAluno = True 
 
        nomeEstudante = input('Digite o nome do estudante: ') 
        emailEstudante = input('Digite o email do estudante: ') 
        senhaEStudante = input('Digite uma senha para o estudante: ') 
 
        novoEstudante = {'id': gerarId(), 'nome': nomeEstudante, 'email': emailEstudante, 'senha': cript(senhaEStudante)} 
 
        estudandes_db.append(novoEstudante) 
 
        print('Novo aluno cadastrado: ', novoEstudante['nome'])

        input('\nPressione ENTER para voltar ao menu...') 
 
    elif (escolha == 2): 
        for aluno in estudandes_db: 
            print(f"{aluno['id']}: {aluno['nome']}") 
 
        IdParaExcluir = input('Escolha o aluno que deseja excluir (id): ') 
 
        for aluno in estudandes_db:
            if aluno['id'] == IdParaExcluir:
                alunoParaExcluir = aluno

            resposta = input(
                f"Tem certeza que deseja excluir o aluno: {alunoParaExcluir['nome']} (s/n): "
            )

            if resposta.lower() == 's':
                estudandes_db.remove(alunoParaExcluir)
                print('Aluno excluido com sucesso')
            else:
                print('Exclusão cancelada')

            break

        input('\nPressione enter para voltar')
 
    elif (escolha == 3):
        for aluno in estudandes_db:
            print(aluno)

        input('\nPressione enter para voltar')

    elif (escolha == 4):
        sistema = False
        print('Sistema encerrado.')

    else:
        print('Opção inválida!')