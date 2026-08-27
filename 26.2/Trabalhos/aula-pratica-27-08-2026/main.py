from assinante import Assinante
from plataforma import PlataformaStreaming

sistema = True
plataforma = PlataformaStreaming()

while sistema:
    print('1. Cadastrar Novo Assinante')
    print('2. Listar Assinantes')
    print('3. Cancelar Assinatura (Excluir)')
    print('4. Sair do Sistema (exibindo o relatório final)')

    resposta = input('Selecione uma Opção: ')

    if resposta == '1':
        nome = input('Nome: ')
        plano = input('Plano (Básico, Padrão ou Premium): ')
        senha = input('Criar Senha: ')

        novoAssinante = Assinante(nome, plano, senha)
        plataforma.cadastrar_assinante(novoAssinante)
        print('Assinante Cadastrado com Sucesso!')
        input('\nPressione Enter para voltar...')

    elif resposta == '2':
        plataforma.listar_assinantes()
        input('\nPressione Enter para voltar...')

    elif resposta == '3':
        plataforma.listar_assinantes()
        idAssinanteExcluir = int(input('Digite o id para excluir: '))
        plataforma.cancelar_assinatura(idAssinanteExcluir)
        input('\nPressione Enter para voltar...')

    elif resposta == '4':
        print('Sistema Encerrado')
        sistema = False

    else:
        print('Valor invalido!')
        input('\nPressione Enter para voltar...')