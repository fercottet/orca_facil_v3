"""
Módulo Base de Widgets.
Responsabilidade: Classe de suporte para widgets personalizados.
Fornece integração com o sistema de temas (InterfaceVisual),
com acesso centralizado às configurações de interface (cores, fontes, janelas).

> Por que não herdamos diretamente de CTkWidget aqui?
Porque WidgetTematico é uma classe abstrata de lógica, não um componente gráfico.
Os componentes visuais (BotaoPadrao, LabelTitulo, etc.) é que herdarão tanto de WidgetTematico quanto do widget real.
"""

from src.configs.interface import InterfaceVisual  # e aplica as cores e fontes vindas de InterfaceVisual
from abc import ABC, abstractmethod


def console(mensagem) -> None:
    print(f"\033[35m[CONTROLLER] {mensagem}.\033[0m")  # Print em CIANO no console

class BaseWidget(ABC):
    """
    Classe Estrutural Abstrata (serve como modelo, não para uso direto).
    Padroniza como os widgets são criados e gerenciados.

    Fornece a estrutura mínima que todos widgets devem seguir:
      - Guardar a instância de InterfaceVisual (com tema, fontes, cores)
      - Implementar o metodo obrigatório aplicar_estilo(), responsável por
        configurar o estilo visual do widget conforme o tema atual.

    Essa classe não herda de customtkinter (CTk), pois serve como uma
    camada puramente lógica — uma "interface" para widgets visuais.

    Herdar de ABC torna a classe abstrata, impedindo que ela seja instanciada diretamente.
    Só subclasses que implementarem aplicar_estilo() poderão ser criadas.
    """
    def __init__(self, interface: InterfaceVisual) -> None:
        """
        :param interface: Objeto de InterfaceVisual contendo configurações visuais (cores, fontes, etc.).
        """
        self.interface = interface

    @abstractmethod
    def aplicar_estilo(self) -> None:
        """
        Metodo abstrato que cada widget deve implementar.
        Define como o widget aplica as suas cores, fontes e demais estilos visuais.

        Ao herdar BaseWidget, o widget é obrigado a sobrescrever este metodo.
        """
        pass

    def atualizar(self) -> None:
        """
        Metodo opcional para forçar atualização visual, de atributo, ou conteúdo.
        Pode ser sobrescrito quando necessário.
        """
        pass


class TemaWidget:
    """
    Classe base para todos os widgets personalizados.

    Oferece acesso às configurações visuais definidas em InterfaceVisual
    e métodos auxiliares para aplicar estilos consistentes.
    """

    def __init__(self, interface: InterfaceVisual) -> None:
        """
        Classe Visual.
        Inicializa o widget temático base.

        :param interface: Instância de InterfaceVisual contendo cores, fontes e estilos do programa.
        """
        self.interface = interface
