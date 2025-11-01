"""
Módulo Controller.
Responsabilidade: Fazer a ponte entre a View e o Model,
controlando o fluxo da aplicação (inicialização, comandos e eventos).
"""

from src.orca_facil.view.principal import JanelaPrincipal
from src.configs.interface import InterfaceVisual, Janelas, Cores, Fontes

def console(mensagem) -> None:
    print(f"\033[34m[CONTROLLER] {mensagem}.\033[0m")  # Print em AZUL no console

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

        # Cria as instâncias de configuração
        self.janelas = Janelas()
        self.cores = Cores()
        self.fontes = Fontes()

        # Junta tudo em um único objeto de interface
        self.interface = InterfaceVisual(
            janelas=self.janelas,
            cores=self.cores,
            fontes=self.fontes,
        )

    def iniciar(self) -> None:
        """
        Inicia a aplicação e aplica as configurações visuais.
        """
        console("Iniciando Controlador")

        # Instancia a Janela Principal (View)
        console("Instanciando View - JanelaPrincipal")
        self.view = JanelaPrincipal(interface=self.interface, janela=self.janelas)
        console("JanelaPrincipal instanciada")

        # Aplica a configuração de cores e o tema ao programa
        self.view.aplicar()
        console("Tema aplicado")

        # Inicia o loop principal do programa com as configurações aplicadas
        console("Inicialização concluída")
        console("Executando aplicação")
        print("\n========== - ========== - ========== - ==========\n")
        self.view.mainloop()
