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


class BaseWidget:
    """
    Classe Estrutural Abstrata (serve como modelo, não para uso direto).
    Padroniza como os widgets são criados e gerenciados.
    Classe base para qualquer widgets do projeto.
    """
    def __init__(self, interface: InterfaceVisual) -> None:
        self.interface = interface

    def aplicar_estilo(self) -> None:
        """
        Metodo genérico para aplicar cores, fontes e dimensões do tema atual.
        Deve ser sobrescrito nas subclasses.
        """

        """
        Se alguém tentar instanciar ou usar aplicar_estilo() sem sobrescrever, o Python avisará.
        É uma forma simples de garantir que quem herdar da classe obrigatoriamente defina esse método
        'raise NotImplementedError' é um “pass" com alarme. Protege de bugs silenciosos.
        """
        raise NotImplementedError("Subclasses devem implementar 'aplicar_estilo'.")


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
