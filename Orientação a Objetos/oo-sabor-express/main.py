from modelos.restaurante import Restaurante

def bootstrap_data():
    restaurante_praca = Restaurante("Praça", "Gourmet")
    restaurante_mexicano = Restaurante("Mexican Food", "Mexicana")
    restaurante_japones = Restaurante("Japa", "Japonesa")

    restaurante_mexicano.alternar_estado()

    restaurante_mexicano.receber_avaliacao("Vianna", 5, "Comida excelente, recomendo o taco!")
    restaurante_mexicano.receber_avaliacao("João", 4, "Muito bom, mas demorou um pouco.")
    restaurante_mexicano.receber_avaliacao("Maria", 2.5, "Achei a pimenta exagerada.")
    restaurante_mexicano.receber_avaliacao("Paulo", 1, "Péssimo atendimento.")
    
    restaurante_praca.receber_avaliacao("Ana", 4.5, "Ambiente agradável.")

def main():
    bootstrap_data()
    print("\n--- Sabor Express | Gerenciamento de Restaurantes ---")
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()