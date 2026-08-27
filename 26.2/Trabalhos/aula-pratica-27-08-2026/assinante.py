import secrets
import hashlib

class Assinante:
    def __init__(self, nome: str, plano: str, senha_plana: str):
        self.id_conta = secrets.choice(range(1000, 10000))
        self.nome = nome
        self.plano = plano
        self.senha_hash = self._gerar_hash(senha_plana)

    def _gerar_hash(self, senha_plana: str) -> str:
        hash_obj = hashlib.sha256()
        hash_obj.update(senha_plana.encode('utf-8'))
        return hash_obj.hexdigest()

    def exibir_dados(self) -> str:
        return (f"ID: {self.id_conta} | "
                f"Nome: {self.nome} | "
                f"Plano: {self.plano} | "
                f"Senha (Hash): {self.senha_hash[:15]}...")