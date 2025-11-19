"""
Módulo View.
Responsabilidade: Criar a Janela Principal do programa e organizar os widgets nela.
"""

import customtkinter as ctk
from src.configs.interface import Janelas, InterfaceVisual
from src.orca_facil.view.widgets.fabrica import FabricaWidgets
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

        # 3. Instancia o tema do programa
        console("Inicialização: 3. Aplicando tema")
        self.aplicar_tema()

        # 4. Configurações globais da Janela Principal
        console("Inicialização: 4. Setando configurações globais da janela principal")
        self.resizable(False, False)
        caminho_icone = os.path.join(caminho_base(), "assets", "icon", "icone.ico")
        self.iconbitmap(caminho_icone)

        # 4.1. Define o título da Janela Principal (parte superior)
        console("Inicialização: 4.1. Definindo título da Janela Principal")
        self.title("Orça Fácil 3.0")

        # 4.2. Define dimensões e posicionamento da Janela Principal (largura x altura + pos_horizontal + pos_vertical)
        dimensao = f"{self.interface.janelas.dimensao_principal}"
        posicao_central = self.centralizar()
        console("Inicialização: 4.2. Dimensionando e centralizando a Janela Principal")
        self.geometry(f"{dimensao}+{posicao_central}")

        # 5. Criar widgets
        console("Inicialização: 5. Instanciando widgets. Chamando Fábrica de Widgets")
        self._instanciar_widgets()

    # CONFIGURAÇÕES
    def obter_dpi_sistema(self) -> float:
        """Retorna o fator de escala do monitor principal (1.0 = 100%)."""

        console("Inicialização - 4.1.2.1. DPI: Obtendo DPI da tela (Configuração de escala de tela do Windows)")
        dpi = self.winfo_fpixels('1i')  # converte "1i" (1 polegada) em pixels reais

        return dpi / 96  # 96 dpi = escala 100% - padrão do Windows
    def centralizar(self) -> str:
        """Centralizada a Janela Principal na tela"""

        # 1. Coleta as dimensões da tela
        console("Inicialização - 4.1.1. Centralização: Coletando dimensões da tela")
        largura_tela = self.winfo_screenwidth()
        altura_tela = self.winfo_screenheight()

        # 2. Obtém o ajuste da configuração de escala de tela do Windows
        console("Inicialização - 4.1.2. Centralização: Ajustando DPI do sistema para tela")
        dpi_ajustado = self.obter_dpi_sistema()

        # 3. Corrigindo largura e altura da tela conforme o DPI
        console("Inicialização - 4.1.3. Centralização: Corrigindo dimensões pelo DPI do sistema")
        largura_corrigida = int(self.janela.largura_principal * dpi_ajustado)
        altura_corrigida = int(self.janela.altura_principal * dpi_ajustado)

        # 4. Calcula a posição central
        console("Inicialização - 4.1.4. Centralização: Calculando posição central")
        pos_x = (largura_tela - largura_corrigida) // 2
        pos_y = (altura_tela - altura_corrigida) // 3

        return f"{pos_x}+{pos_y}"
    def aplicar_tema(self) -> None:
        """
        Usar as informações de 'Configs/interface.py' para configurar o tema global
        Configura o modo (claro/escuro) e o esquema de cores principal.
        """

        # 1. Define o modo de cor do programa (Light, Dark ou System)
        ctk.set_appearance_mode(self.janela.modo)
        console(f"[VIEW] Inicialização: 3.1. TEMA - Modo de cor selecionado: {self.janela.modo.capitalize()}")

        # 2. Define o tema de cores do programa
        self.interface.tema.aplicar_tema(f"{self.interface.tema.tema_atual}")
        console(f"[VIEW] Inicialização: 3.2. TEMA - Tema de cores carregado: {self.interface.tema.tema_atual}")

    # WIDGETS
    def _instanciar_widgets(self) -> None:
        """
        Metodo Privado.
        Cria e posiciona widgets principais da janela.
        """

        self.fabrica = FabricaWidgets()

        def botoes():
            self.botao_novo_orcamento = self.fabrica.criar_botao(
                master=self,
                texto="Novo\nOrçamento",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=25, y=50
            )

            self.botao_adicionar_arquivos = self.fabrica.criar_botao(
                master=self,
                texto="Adicionar\nArquivos",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=200, y=50
            )

            self.botao_carregar_perfil = self.fabrica.criar_botao(
                master=self,
                texto="Carregar Perfil",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=25, y=120
            )

            self.botao_tamanhos_e_quantidades = self.fabrica.criar_botao(
                master=self,
                texto="Tamanhos e\nQuantidades",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=200, y=120
            )

            self.botao_configuracoes = self.fabrica.criar_botao(
                master=self,
                texto="Configurações",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=25, y=190
            )

            self.botao_gerar_pdf = self.fabrica.criar_botao(
                master=self,
                texto="Gerar PDF",
                interface=self.interface,
                comando=lambda: "",  # 'lambda' para não executar antes de clicar no botão
                x=200, y=190
            )

            return (self.botao_novo_orcamento, self.botao_adicionar_arquivos, self.botao_carregar_perfil,
                    self.botao_tamanhos_e_quantidades, self.botao_configuracoes, self.botao_gerar_pdf)
        def labels():

            # BLOCO PRECIFICAÇÃO ============================
            def labels_texto_precificacao():
                self.label_texto_valor_total = self.fabrica.criar_label(
                    master=self,
                    texto="VALOR TOTAL: R$",
                    interface=self.interface,
                    x=395, y=50
                ).configure(font=(self.interface.fontes.tipo_geral, 20, "bold"), anchor="e")

                self.label_texto_valor_parcelado = self.fabrica.criar_label(
                    master=self,
                    texto="VALOR PARCELADO: R$",
                    interface=self.interface,
                    x=395, y=97.50
                ).configure(anchor="e")

                self.label_texto_em = self.fabrica.criar_label(
                    master=self,
                    texto="EM",
                    interface=self.interface,
                    x=715, y=97.50
                ).configure(width=40)

                self.label_texto_parcelas_de = self.fabrica.criar_label(
                    master=self,
                    texto="PARCELAS DE R$",
                    interface=self.interface,
                    x=795, y=97.50
                ).configure(width=160, anchor="e")

                self.label_texto_pix_dinheiro = self.fabrica.criar_label(
                    master=self,
                    texto="PIX / DINHEIRO: R$",
                    interface=self.interface,
                    x=395, y=145
                ).configure(anchor="e")

                self.label_texto_imposto_nota = self.fabrica.criar_label(
                    master=self,
                    texto="IMPOSTO NOTA: R$",
                    interface=self.interface,
                    x=395, y=192.50
                ).configure(anchor="e")

                self.label_texto_porcentagem_imposto = self.fabrica.criar_label(
                    master=self,
                    texto="% IMPOSTO NOTA:",
                    interface=self.interface,
                    x=795, y=192.50
                ).configure(width=160, anchor="e")

                return (self.label_texto_valor_total, self.label_texto_valor_parcelado, self.label_texto_em,
                        self.label_texto_parcelas_de, self.label_texto_pix_dinheiro, self.label_texto_imposto_nota,
                        self.label_texto_porcentagem_imposto)
            def labels_saida_precificacao():
                self.label_saida_valor_total = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=605, y=58.75
                ).configure(font=(self.interface.fontes.tipo_geral, 20, "bold"), anchor="w",
                            bg_color=self.interface.cores.laranja,
                            width=180, height=30)

                self.label_saida_valor_parcelado = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=605, y=108.75
                ).configure(anchor="w", bg_color=self.interface.cores.cinza_claro, width=110, height=25)

                self.label_saida_parcelas_de = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=965, y=108.75
                ).configure(anchor="w", bg_color=self.interface.cores.cinza_claro, width=110, height=25)

                self.label_saida_pix_dinheiro = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=605, y=156.25
                ).configure(anchor="w", bg_color=self.interface.cores.cinza_claro, width=110, height=25)

                self.label_saida_imposto_nota = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=605, y=203.75
                ).configure(anchor="w", bg_color=self.interface.cores.cinza_claro, width=110, height=25)

                self.label_saida_porcentagem_imposto = self.fabrica.criar_label(
                    master=self,
                    texto="",
                    interface=self.interface,
                    x=965, y=203.75
                ).configure(anchor="w", bg_color=self.interface.cores.cinza_claro, width=110, height=25)

                return self.label_saida_valor_total, self.label_saida_valor_parcelado, self.label_saida_parcelas_de

            # BLOCO INFORMAÇÕES ============================
            def labels_texto_informacoes():
                self.label_orcamento_numero = self.fabrica.criar_label(
                    master=self,
                    texto="ORÇAMENTO Nº:",
                    interface=self.interface,
                    x=1300, y=60
                ).configure(width=145, height=30, anchor="w")

                self.label_perfil = self.fabrica.criar_label(
                    master=self,
                    texto="PERFIL:",
                    interface=self.interface,
                    x=1300, y=90
                ).configure(height=30, anchor="w")

                self.label_cliente = self.fabrica.criar_label(
                    master=self,
                    texto="CLIENTE:",
                    interface=self.interface,
                    x=1300, y=120
                ).configure(height=30, anchor="w")

                self.label_status = self.fabrica.criar_label(
                    master=self,
                    texto="PRONTO PARA COMEÇAR",
                    interface=self.interface,
                    x=1300, y=150
                ).configure(height=50, anchor="center", text_color=self.interface.fontes.fonte_status())

                return self.label_orcamento_numero, self.label_perfil, self.label_cliente
            def labels_saida_informacoes():

                return ""

            self.labels_texto_precificacao = labels_texto_precificacao()
            self.labels_saida_precificacao = labels_saida_precificacao()
            self.labels_texto_informacoes = labels_texto_informacoes()
            self.labels_saida_informacoes = labels_saida_informacoes()

            return (self.labels_texto_precificacao, self.labels_saida_precificacao,
                    self.labels_texto_informacoes, self.labels_saida_informacoes)

        # Chama a função de criação dos Widgets
        self.botoes = botoes()
        self.labels = labels()

    # ESTILOS
    def atualizar_tema(self, novo_tema: str) -> None:
        """
        Metodo público.
        Atualiza estilos quando o tema mudar.
        O Controller poderá chamar este metodo após alterar o tema global.
        """
        self.interface.tema.aplicar_tema(novo_tema)
        self.fabrica.atualizar_tema_widgets()
        console(f"Tema atualizado para: {novo_tema.capitalize()}")