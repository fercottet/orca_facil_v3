"""
Módulo de Fabricação de Widgets
Responsabilidade:
Centralizar a criação, configuração e posicionamento de widgets da interface.
Cada metodo cria um tipo de widget (Botão, Label, Entrada, etc.),
aplicando automaticamente o tema visual e posicionando-o na tela.
"""

from src.orca_facil.view.widgets.botao import Botao
from src.orca_facil.view.widgets.base import console
from src.configs.interface import InterfaceVisual


class FabricaWidgets:
    """
    Fábrica central de widgets.
    Cada metodo estático cria um widget temático e o posiciona conforme parâmetros recebidos.
    """

    # === BOTÃO ===
    @staticmethod
    def criar_botao(master, texto: str, interface: InterfaceVisual, comando=None,
                   x=None, y=None, largura=150, altura=60, **kwargs):
        """
        Cria um botão temático e o posiciona na janela.

        :param: master: Container (janela, frame, etc.) onde o botão será inserido.
        :param: texto: Texto exibido no botão.
        :param: interface: Instância de InterfaceVisual para aplicar estilo.
        :param: comando: Função a ser executada no clique.
        :param: x: Posição absoluta horizontal em relação a margem esquerda da janela (master).
        :param: y: Posição absoluta vertical em relação a margem superior da janela (master).
        :param: largura: Largura do botão (opcional).
        :param: altura: Altura do botão (opcional).
        :param: **kwargs: Parâmetros adicionais repassados ao Botao (como corner_radius, etc.).
        """

        console(f"Fábrica: Criando botão {texto}")

        # 1. Cria o botão
        botao = Botao(master, texto, interface, width=largura, height=altura, comando=comando, **kwargs)

        # 2. Posiciona o botão
        botao.place(x=x, y=y, **kwargs)

        # 3. Retorna o widget criado para eventual manipulação posterior
        return botao