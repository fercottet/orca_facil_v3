"""
Módulo View.
Responsabilidade: Criar a Janela Principal do programa e organizar os widgets nela.
"""

import customtkinter as ctk
from src.configs.interface import Janelas, InterfaceVisual
from src.orca_facil.view.widgets.botao import Botao
import os
import sys


def console(mensagem) -> None:
    print(f"\033[93m[VIEW] {mensagem}.\033[0m")  # Print em AMARELO no console


def caminho_base():
    pasta_view = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.normpath(os.path.join(pasta_view, "..", "..", ".."))


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
        Fundamental quando herdamos classes com muitos parâmetros opcionais, como tkinter e customtkinter.

        A classe JanelaPrincipal herda de ctk.CTk.
        Como CTk aceita muitos parâmetros opcionais (como fg_color, width, height, etc.),
        usar *args e **kwargs permite repasse automático desses argumentos para a superclasse
        sem precisar declarar todos manualmente.
        """
        console("Iniciando Módulo View. Método '__init__()' foi chamado")

        # 1. Chama o construtor da classe-pai (CTk). Sem ele só teríamos uma classe e não uma Janela Principal
        super().__init__(*args, **kwargs)  # Aplica eventuais parâmetros herdados
        console("Inicialização: 1. Chamando o construtor da classe-pai - super().__init__")

        # 2. Instancia as classes de configuração
        console("Inicialização: 2. Instanciando classes de configuração")

        # 2.1. Armazena o objeto de configuração de interface (tema, fontes, cores).
        console("Inicialização: 2.1. Armazenando objeto de configuração de interface (InterfaceVisual)")
        self.interface: InterfaceVisual = interface  # Com notação de tipagem - InterfaceVisual
        """
        <variável>: TIPO = <valor>
        Essa linha chama o construtor da classe pai (CTk) e passa para ela os mesmos argumentos recebidos aqui.
        """

        # 2.2. Instancia as configurações da Janela Principal
        console("Inicialização: 2.2. Instanciando as configurações da janela principal")
        self.janela: Janelas = janela  # Com notação de tipagem - Janelas

        # 3. Configurações globais da Janela Principal
        console("Inicialização: 3. Setando configurações globais da janela principal")
        self.resizable(False, False)
        caminho_icone = os.path.join(caminho_base(), "assets", "icon", "icone.ico")
        self.iconbitmap(caminho_icone)

        # 3.1. Define o título da Janela Principal (parte superior)
        console("Inicialização: 3.1. Definindo título da Janela Principal")
        self.title("Orça Fácil 3.0")

        # 3.2. Define dimensões e posicionamento da Janela Principal (largura x altura + pos_horizontal + pos_vertical)
        dimensao = f"{self.interface.janelas.dimensao_principal}"
        posicao_central = self.centralizar()
        console("Inicialização: 3.2. Dimensionando e centralizando a Janela Principal")
        self.geometry(f"{dimensao}+{posicao_central}")

        # 4. Configurar estilos personalizados
        self._configurar_estilos()

        # 5. Criar widgets
        self._criar_widgets()

    # CONFIGURAÇÕES
    def obter_dpi_sistema(self) -> float:
        """Retorna o fator de escala do monitor principal (1.0 = 100%)."""

        console("Inicialização - DPI: Obtendo DPI da tela (Configuração de escala de tela do Windows)")
        dpi = self.winfo_fpixels('1i')  # converte "1i" (1 polegada) em pixels reais

        return dpi / 96  # 96 dpi = escala 100% - padrão do Windows

    def centralizar(self) -> str:
        """Centralizada a Janela Principal na tela"""

        # 1. Coleta as dimensões da tela
        console("Inicialização - Centralização: Coletando dimensões da tela")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        # 2. Obtém o ajuste da configuração de escala de tela do Windows
        console("Inicialização - Centralização: Ajustando DPI do sistema para tela")
        dpi_ajustado = self.obter_dpi_sistema()

        # 3. Corrigindo largura e altura da tela conforme o DPI
        console("Inicialização - Centralização: Corrigindo dimensões pelo DPI do sistema")
        largura_corrigida = int(self.janela.largura_principal * dpi_ajustado)
        altura_corrigida = int(self.janela.altura_principal * dpi_ajustado)

        # 4. Calcula a posição central
        console("Inicialização - Centralização: Calculando posição central")
        pos_x = (largura_tela - largura_corrigida) // 2
        pos_y = (altura_tela - altura_corrigida) // 3

        return f"{pos_x}+{pos_y}"

    def aplicar(self) -> None:
        """
        Usar as informações de 'Configs/interface.py' para configurar o tema global
        Configura o modo (claro/escuro) e o esquema de cores principal.
        """

        # 1. Define o modo de cor do programa (Light, Dark ou System)
        console("Aplicando Configuração: Modo de cor")
        ctk.set_appearance_mode(self.janela.modo)

        # 2. Define o tema de cores do programa
        console("Aplicando Configuração: Tema de cores")
        ctk.set_default_color_theme("green")

    # WIDGETS
    def _criar_widgets(self) -> None:
        """
        Metodo Privado.
        Cria e posiciona widgets principais da janela.
        """
        self.botao_teste_1 = Botao(self, "Teste", interface=self.interface)
        self.botao_teste_1.pack(pady=20)

        self.botao_teste_2 = Botao(self, "Teste", interface=self.interface)
        self.botao_teste_2.pack(pady=20)
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
