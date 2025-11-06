"""
Módulo de Botões da interface visual.
Responsabilidade: Define o widget temático de botão que aplica automaticamente
o estilo visual fornecido por uma instância de InterfaceVisual.
"""

from customtkinter import CTkButton
from src.orca_facil.view.widgets.base import BaseWidget, console
from src.configs.interface import InterfaceVisual


class Botao(BaseWidget, CTkButton):
    """
    Classe que representa um botão integrado ao sistema visual da aplicação.
    Herda de BaseWidget (módulo Widgets) e de CTkButton (widget visual do CustomTkinter).
    """

    def __init__(self, local, texto:str, interface:InterfaceVisual, comando=None, **kwargs):
        """
        Inicializa o botão temático aplicando automaticamente o estilo definido pelo tema.

        Args:
            local: Container (janela, frame, etc.) que conterá o botão.
            texto: Texto exibido no botão.
            tema: Instância de InterfaceVisual usada para aplicar o estilo.
            comando: Função a ser executada quando o botão for clicado.
            **kwargs: Parâmetros opcionais adicionais do CTkButton.
        """

        console("Botão: Classe 'Botao' iniciada")

        # 1. Inicialize as heranças
        BaseWidget.__init__(self, interface)
        CTkButton.__init__(self, master=local, text=texto, command=comando, **kwargs)

        # 2. Guarda as referências
        self.local = local
        self.texto = texto
        self.comando = comando
        self.interface = interface

        # 3. Aplicar tema de cor
        self.interface.tema.aplicar_tema(self.interface.tema.tema_atual)

        # 4. Aplica o estilo geral ao botão
        self.aplicar_estilo()

    def aplicar_estilo(self) -> None:
        """
        Atualiza dinamicamente o estilo do botão conforme o tema atual.
        Pode ser chamado quando o tema é alterado em tempo de execução.
        """

        console("Botão - Aplicando estilo")

        self.configure(
            fg_color=self.interface.tema.cor_principal,
            hover_color=self.interface.tema.cor_principal_hover,
            corner_radius=self.interface.gerais.raio_canto,
            font=self.interface.fontes.fonte_botao
        )

