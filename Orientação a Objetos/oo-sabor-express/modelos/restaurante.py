from typing import List, Optional
from modelos.avaliacao import Avaliacao

class Restaurante:
    _restaurantes: List['Restaurante'] = []

    def __init__(self, nome: str, categoria: str) -> None:
        if not nome or not categoria:
            raise ValueError("Nome e Categoria são campos obrigatórios.")
        
        self._nome = nome.strip().title()
        self._categoria = categoria.strip().upper()
        self._ativo = False
        self._avaliacoes: List[Avaliacao] = []

        self._soma_notas = 0.0
        
        Restaurante._restaurantes.append(self)

    def __str__(self) -> str:
        return f"{self._nome} | {self._categoria}"

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def categoria(self) -> str:
        return self._categoria

    @property
    def ativo(self) -> str:
        return 'Ativado' if self._ativo else 'Desativado'

    @property
    def media_avaliacoes(self) -> float:
        if not self._avaliacoes:
            return 0.0
        return round(self._soma_notas / len(self._avaliacoes), 1)

    def alternar_estado(self) -> None:
        self._ativo = not self._ativo

    def receber_avaliacao(self, cliente: str, nota: float, comentario: str) -> None:
        nova_avaliacao = Avaliacao(cliente, nota, comentario)
        self._avaliacoes.append(nova_avaliacao)
        self._soma_notas += nova_avaliacao.nota

    @classmethod
    @property
    def todos(cls) -> List['Restaurante']:
        return cls._restaurantes

    @classmethod
    def listar_restaurantes(cls) -> None:
        header = f"{'Nome do restaurante'.ljust(25)} | {'Categoria'.ljust(25)} | {'Avaliação'.ljust(25)} | {'Status'}"
        print(f"\n{header}")
        print("-" * len(header))
        
        for restaurante in cls._restaurantes:
            media = str(restaurante.media_avaliacoes) if restaurante.media_avaliacoes > 0 else 'Sem Avaliação'
            print(f"{restaurante.nome.ljust(25)} | {restaurante.categoria.ljust(25)} | {media.ljust(25)} | {restaurante.ativo}")