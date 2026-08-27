from assinante import Assinante

class PlataformaStreaming:
    def __init__(self):
        self.assinantes = []

    def cadastrar_assinante(self, assinante: Assinante):
        self.assinantes.append(assinante)
        print(f"Assinante {assinante.nome} cadastrado com sucesso! ID: {assinante.id_conta}")

    def listar_assinantes(self):
        if not self.assinantes:
            print("Nenhum assinante cadastrado no momento.")
            return

        print("LISTA DE ASSINANTES ATIVOS")
        for assinante in self.assinantes:
            print(assinante.exibir_dados())

    def buscar_por_id(self, id_conta: int) -> Assinante:
        for assinante in self.assinantes:
            if assinante.id_conta == id_conta:
                return assinante
        return None

    def cancelar_assinatura(self, id_conta: int) -> bool:
        assinante_para_remover = self.buscar_por_id(id_conta)
        
        if assinante_para_remover:
            self.assinantes.remove(assinante_para_remover)
            return True
            
        return False