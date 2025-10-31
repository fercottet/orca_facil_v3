"""
Módulo View.
Responsabilidade: Criar a Janela Principal do programa e organizar os widgets nela.
"""

import customtkinter as ctk
from src.configs.interface import Janelas, InterfaceVisual

class JanelaPrincipal(ctk.CTk):
    """
    Recebe uma instância de InterfaceVisual com as configurações (tema, fontes, cores).
    Responsabilidades iniciais:
      - aplicar dimensões e título
      - cria metodo privado para configurar estilos
      - cria metodo privado para instanciar widgets
      - expõe um metodo público para atualizar estilos (chamado pelo Controller quando necessário)
    """

    # INICIALIZAÇÃO
    def __init__(self, interface: InterfaceVisual, janela: Janelas, *args, **kwargs) -> None:
        """
        Inicializa a janela principal.

        :param interface: Objeto com configurações de janelas, cores e fontes.
        :param args: Argumentos posicionais variáveis opcionais passados à classe-pai CTk. Empacota tudo numa tupla.
        :param kwargs: Argumentos nomeados variáveis opcionais passados à classe-pai CTk. Empacota tudo num dicionário.

        Juntos, *args e **kwargs tornam o construtor flexível e expansível.
        Fundamental quando herdamos classes que têm muitos parâmetros opcionais, como tkinter e customtkinter.

        A classe JanelaPrincipal herda de ctk.CTk.
        Como CTk aceita muitos parâmetros opcionais (como fg_color, width, height, etc.),
        usar *args e **kwargs permite repasse automático desses argumentos para a superclasse
        sem precisar declarar todos manualmente.
        """
        print("[VIEW] Iniciando Módulo View. Método '__init__()' foi chamado.")

        # 1. Chama o construtor da classe-pai (CTk). Sem ele só teríamos uma classe e não uma Janela Principal
        super().__init__(*args, **kwargs)  # Aplica eventuais parâmetros herdados
        print("[VIEW] Inicialização: 1. Chamando o construtor da classe-pai - super().__init__")

        # 2. Instancia as classes de configuração
        print("{VIEW] 2. Instanciando classes de configuração.")

        # 2.1. Armazena o objeto de configuração de interface (tema, fontes, cores).
        print("[VIEW] Inicialização: 2.1. Armazenando objeto de configuração de interface (InterfaceVisual)")
        self.interface: InterfaceVisual = interface  # Com notação de tipagem - InterfaceVisual
        """
        <variável>: TIPO = <valor>
        Essa linha chama o construtor da classe pai (CTk) e passa para ela os mesmos argumentos recebidos aqui.
        """

        # 2.2. Instancia as configurações da Janela Principal
        print("[VIEW] Inicialização: 2.2. Instanciando as configurações da janela principal")
        self.janela: Janelas = janela  # Com notação de tipagem - Janelas

        # 3. Configurações globais da Janela Principal
        print("[VIEW] Inicialização: 3. Setando configurações globais: Título e dimensões da janela principal")
        self.title("Orça Fácil 3.0")  # Título da janela (parte superior)
        self.geometry(self.interface.janelas.dimensao_principal)  # Dimensões (em pixels) da Janela - Largura x Altura.

        # 4. Configurar estilos personalizados
        self._configurar_estilos()

        # 5. Criar widgets
        self._criar_widgets()

    # CONFIGURAÇÕES
    def aplicar(self) -> None:
        """
        Usar as informações de 'Configs/interface.py' para configurar o tema global
        Configura o modo (claro/escuro) e o esquema de cores principal.
        """

        # 1. Define o modo de cor do programa (Light, Dark ou System)
        print("[VIEW] Aplicando Configurações: Modo de Cor")
        ctk.set_appearance_mode(self.janela.modo)

        # 2. Define o tema de cores do programa
        print("[VIEW] Aplicando Configurações: Tema de cores")
        ctk.set_default_color_theme("green")


    # WIDGETS
    def _criar_widgets(self) -> None:
        """
        Metodo Privado.
        Cria e posiciona widgets principais da janela.
        """

        pass

    # ESTILOS
    def _configurar_estilos(self) -> None:
        """
        Metodo Privado.
        Configura estilos globais (registrar ttk styles, fontes, etc.).
        """

        pass
    def atualizar_estilos(self) -> None:
        """
        Metodo público.
        Atualiza estilos quando o tema mudar.
        O Controller poderá chamar este metodo após alterar o tema global.
        """

        # aqui vamos iterar por widgets ou reconfigurar o que for necessário
        pass

