"""
Módulo de inicialização.
Responsabilidade: Instanciação do Controller e inicialização da interface por meio dele (Main → Controller → View)
"""

# Importa a classe Controller responsável por gerenciar o fluxo da aplicação
from src.orca_facil.controller.controller import Controller
""" 'from' <pasta> → <pasta> → <pasta> → <módulo> 'import' <Classe> """

def console(mensagem) -> None:
    print(f"\033[95m[MAIN] {mensagem}.\033[0m")  # Print em MAGENTA no console

def main() -> None:
    """
    Instancia o Controller, inicializa a interface e o loop principal do programa.
    """

    controller = Controller()  # Instancia o Controller (<variável> = <Classe> importada
    console("Controller instanciado")

    console("Iniciando processo de carregamento da Janela Principal")
    controller.iniciar()  # Chama o metodo de inicialização do programa, que cria a janela principal e os seus widgets


if __name__ == "__main__":  # Garante que "main()" só será executado se for rodado diretamente (não quando importado)
    console("Inicializando..")
    main()  # Executa a aplicação
