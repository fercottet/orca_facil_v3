"""
Módulo Controller.
Responsabilidade: Fazer a ponte entre a View e o Model,
controlando o fluxo da aplicação (inicialização, comandos e eventos).
"""

from src.orca_facil.view.principal import JanelaPrincipal
from src.configs.interface import InterfaceVisual

def console(mensagem) -> None:
    print(f"\033[94m[CONTROLLER] {mensagem}.\033[0m")  # Print em AZUL no console

class Controller:
    """
    Classe principal do Controller.
    Gerencia a inicialização da interface e coordena a comunicação entre View e Model.
    """

    def __init__(self) -> None:
        """
        Construtor do Controller.
        Gerencia a inicialização da interface e coordena a comunicação entre View e Model.
        """

        self.view = None  # Referência à View principal (criada no metodo iniciar) - Inicialização da variável

        # Cria as instâncias de configuração e junta tudo em um único objeto de interface
        self.interface = InterfaceVisual()

    def iniciar(self) -> None:
        """
        Inicia a aplicação e aplica as configurações visuais.
        """
        console("Iniciando Controlador")

        # 1. Instancia a Janela Principal (View)
        console("Instanciando View - JanelaPrincipal")
        self.view = JanelaPrincipal(interface=self.interface, janela=self.interface.janelas)
        console("JanelaPrincipal instanciada")

        # 2. Inicia o loop principal do programa com as configurações aplicadas
        console("Inicialização concluída")
        console("Executando aplicação")
        print("\n========== - ========== - ========== - ==========\n")
        self.view.mainloop()
