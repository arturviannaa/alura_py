from dataclasses import dataclass

@dataclass(frozen=True)
class Avaliacao:
    cliente: str
    nota: float
    comentario: str

    def __post_init__(self):
        object.__setattr__(self, 'nota', max(0.0, min(5.0, float(self.nota))))
        
        if not self.comentario:
            raise ValueError("O comentário da avaliação é obrigatório.")