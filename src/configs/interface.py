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
    azul_claro: str = "#4CABFF"
    azul_escuro: str = "#1F6EB3"
    laranja: str = "#C25912"
    roxo_claro: str = "#7B2CBF"
    roxo_escuro: str = "#5A189A"
    verde_claro: str = "#2EC233"
    verde_escuro: str = "#117014"


@dataclass
class Fontes:
    """Define tipos, tamanhos e cores das fontes do programa"""

    tipo_geral: str = "verdana"

    # PADRÃO =============================================
    tipo_padrao: str = tipo_geral
    tamanho_padrao: int = 12
    negrito_padrao: str = ""

    @property
    def fonte_padrao(self) -> tuple:
        """Configura o padrão de tipo, tamanho e negrito da fonte do programa"""
        return self.tipo_padrao, self.tamanho_padrao, self.negrito_padrao

    # TÍTULO =============================================
    tipo_titulo: str = tipo_geral
    tamanho_titulo: int = 16
    negrito_titulo: str = "bold"

    @property
    def fonte_titulo(self) -> tuple:
        """Configura o tipo, tamanho e negrito da fonte para títulos"""
        return self.tipo_titulo, self.tamanho_titulo, self.negrito_titulo

    # BOTÕES =============================================
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
class Tema:
    """Define as cores do programa e permite alterar entre temas."""

    # Instancia a classe de cores.
    cor = Cores()

    # Cria a lista de temas disponíveis
    lista_tema: list[str] = field(default_factory=lambda: ["Azul", "Verde", "Roxo"])
    """
    O parâmetro default_factory do field() espera uma função (callable)
    Isto é, algo que possa ser chamado para gerar o valor padrão.
    Ou seja, ele precisa de uma função que retorne o valor desejado.
    lambda: ["Azul", "Verde", "Roxo"] é uma função anônima.
    Ela será chamada quando o objeto for criado, retornando uma nova lista.
    ["Azul", "Verde", "Roxo"] é apenas uma lista — um objeto pronto, não chamável.
    """

    # Define o tema atual
    tema_atual: str = "Verde"

    # Atributos explicitamente definidos
    cor_principal: str = f"{cor.verde_escuro}"
    cor_principal_hover: str = f"{cor.verde_claro}"
    cor_destaque: str = f"{cor.laranja}"

    # Define as cores globais conforme o tema escolhido, sem alterar diretamente os widgets.
    def aplicar_tema(self, tema: str = f"{tema_atual}") -> None:
        """
        Redefine as cores-base do programa conforme o tema selecionado.

        Responsabilidade:
            Este metodo atua no nível de configuração global, ajustando
            os valores de cor associados ao tema ativo (ex.: Verde, Azul, Roxo).
            Ele não altera diretamente a aparência dos widgets — apenas
            atualiza os atributos de cor que os widgets usam ao aplicar
            o seu próprio estilo.

        Uso típico:
            Chamado quando o usuário troca o tema do programa.
            Após a chamada, cada widget deve atualizar a sua aparência
            executando o metodo 'aplicar_estilo()'.

        Args:
            tema (str): Nome do tema a ser aplicado. Caso omitido, mantém o tema atual.
        Raises:
            ValueError: Se o nome informado não corresponder a nenhum tema disponível.
        """

        if tema:
            self.tema_atual = tema.capitalize()  # Para garantir consistência com 'Verde', 'Azul', etc.

        if tema == "Verde":
            self.cor_principal = f"{self.cor.verde_escuro}"
            self.cor_principal_hover = f"{self.cor.verde_claro}"
            self.cor_destaque = f"{self.cor.laranja}"

        elif tema == "Azul":
            self.cor_principal = f"{self.cor.azul_escuro}"
            self.cor_principal_hover = f"{self.cor.azul_claro}"
            self.cor_destaque = f"{self.cor.laranja}"

        elif tema == "Roxo":
            self.cor_principal = f"{self.cor.roxo_escuro}"
            self.cor_principal_hover = f"{self.cor.roxo_claro}"
            self.cor_destaque = f"{self.cor.laranja}"

        else:
            raise ValueError(f"Tema '{tema}' não encontrado. Temas disponíveis: {', '.join(self.lista_tema)}")

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

    # Cria instâncias próprias para cada configuração visual, evitando que alterações em uma afetem as demais.
    janelas: Janelas = field(default_factory=Janelas)
    cores: Cores = field(default_factory=Cores)
    fontes: Fontes = field(default_factory=Fontes)
    gerais: Gerais = field(default_factory=Gerais)
    tema: Tema = field(default_factory=Tema)
