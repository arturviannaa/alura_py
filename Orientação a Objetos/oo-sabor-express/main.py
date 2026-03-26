from modelos.restaurante import Restaurante

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
restaurante_japones = Restaurante("Japa", "Japonesa")

restaurante_mexicano.alternar_estado()

restaurante_praca.receber_avaliacao("Vianna", 10)
restaurante_praca.receber_avaliacao("João", 8)
restaurante_praca.receber_avaliacao("Maria", 5)
restaurante_praca.receber_avaliacao("Paulo", 3)

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()