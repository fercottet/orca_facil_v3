"""
Módulo de configurações visuais.
Responsabilidade: Centralizar e simplificar a criação e manutenção das configurações visuais do programa.
"""

from dataclasses import dataclass, field


@dataclass
class Janelas:
    """Define as características da janela principal e modais do programa."""

    modo: str = field(default="dark")  # 'light' (claro) ou 'dark' (escuro)

    # DIMENSÕES
    largura_principal: int = 1440
    altura_principal: int = 780

    @property
    def dimensao_principal(self) -> str:
        """Obtém a dimensão da Janela Principal"""
        return f"{self.largura_principal}x{self.altura_principal}"


@dataclass
class Cores:
    """Relaciona nomes de cores com seus respectivos códigos hexadecimais para facilitar a leitura."""
    laranja: str = "#C25912"
    verde_claro: str = "#2F7C32"
    verde_escuro: str = "#154209"


@dataclass
class Fontes:
    """Define tipos, tamanhos e cores das fontes do programa"""

    tipo_geral: str = "verdana"

    # PADRÃO
    tipo_padrao: str = tipo_geral
    tamanho_padrao: int = 12
    negrito_padrao: str = ""

    @property
    def fonte_padrao(self) -> tuple:
        """Configura o padrão de tipo, tamanho e negrito da fonte do programa"""
        return self.tipo_padrao, self.tamanho_padrao, self.negrito_padrao

    # TÍTULO
    tipo_titulo: str = tipo_geral
    tamanho_titulo: int = 16
    negrito_titulo: str = "bold"

    @property
    def fonte_titulo(self) -> tuple:
        """Configura o tipo, tamanho e negrito da fonte para títulos"""
        return self.tipo_titulo, self.tamanho_titulo, self.negrito_titulo

    # BOTÕES
    tipo_botao: str = tipo_geral
    tamanho_botao: int = 14
    negrito_botao: str = "bold"

    @property
    def fonte_botao(self) -> tuple:
        """Padroniza tipo, tamanho e negrito dos botões"""
        return self.tipo_botao, self.tamanho_botao, self.negrito_botao


@dataclass
class Gerais:
    """ Define outras características dos widgets."""
    raio_canto = 10

@dataclass
class InterfaceVisual:
    """
    Container de configurações visuais do programa.

    Responsabilidade:
        - Reunir, em uma única estrutura, os objetos de configuração (Janelas, Cores e Fontes)
          para facilitar o transporte e a leitura pelo Controller e pela View.

    Observação:
        Esta classe não aplica temas nem executa lógica visual — apenas fornece os dados necessários.
    """

    # INSTÂNCIAS
    janelas: Janelas
    cores: Cores
    fontes: Fontes
    gerais: Gerais
