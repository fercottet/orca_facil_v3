"""
Módulo de Labels da interface visual.
Responsabilidade: Define o widget temático de label que aplica automaticamente
o estilo visual fornecido por uma instância de InterfaceVisual.
"""

from customtkinter import CTkLabel
from src.orca_facil.view.widgets.base import BaseWidget, console
from src.configs.interface import InterfaceVisual


class Label(BaseWidget, CTkLabel):
    """
    Classe que representa um botão integrado ao sistema visual da aplicação.
    Herda de BaseWidget (módulo Widgets) e de CTkButton (widget visual do CustomTkinter).
    """

    def __init__(self, local, texto:str, interface:InterfaceVisual, **kwargs):
        """
        Inicializa o label temático aplicando automaticamente o estilo definido pelo tema.

        Args:
            local: Container (janela, frame, etc.) que conterá o label.
            texto: Texto exibido no label.
            tema: Instância de InterfaceVisual usada para aplicar o estilo.
            **kwargs: Parâmetros opcionais adicionais do CTkLabel.
        """

        console("Label: Classe 'Label' iniciada")

        # 1. Inicialize as heranças
        BaseWidget.__init__(self, interface)
        CTkLabel.__init__(self, master=local, text=texto, **kwargs)

        # 2. Guarda as referências
        self.local = local
        self.texto = texto
        self.interface = interface

        # 3. Aplica o estilo geral ao label
        self.aplicar_estilo()

    def aplicar_estilo(self) -> None:
        """
        Atualiza dinamicamente o estilo do label conforme o tema atual.
        Pode ser chamado quando o tema é alterado em tempo de execução.
        """

        console("Label - Aplicando estilo ao label")

        self.configure(
            font=self.interface.fontes.fonte_label
        )
