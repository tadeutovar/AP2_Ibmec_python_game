
largura_layout = 70
def gera_layout(textos_coluna1, textos_coluna2, titulo="", n_sequencia=""):
    """
    Gera um retângulo com bordas, um título e dois conjuntos de textos organizados em colunas.

    :param textos_coluna1: Lista de strings para a primeira coluna.
    :param textos_coluna2: Lista de strings para a segunda coluna.
    :param largura_layout: Largura do retângulo.
    :param titulo: Título a ser exibido na linha superior.
    :param n_sequencia: Posição do retângulo na sequência ("inicio", "meio", "final").
    """
    largura_layout = 70
    # Ajusta a largura para ímpar se necessário
    if largura_layout % 2 == 0:
        largura_layout += 1
    largura_coluna = (largura_layout // 2) - 1

    # Linha superior com título
    if not (n_sequencia == "meio" or n_sequencia == "final"):
        espaco_titulo = (largura_layout - len(titulo) - 2) // 2
        linha_titulo = "═" * espaco_titulo +  titulo  + "═" * espaco_titulo

        # Ajusta a linha se a largura do título for ímparthal
        if len(linha_titulo) < largura_layout - 2:
            linha_titulo += "═"
        print()
        print("╔" + linha_titulo + "╗")

    # Linhas com textos
    max_linhas = max(len(textos_coluna1), len(textos_coluna2))
    for i in range(max_linhas):
        texto1 = textos_coluna1[i] if i < len(textos_coluna1) else ""
        texto2 = textos_coluna2[i] if i < len(textos_coluna2) else ""
        linha = "║ " + texto1.ljust(largura_coluna - 1)
        linha += "  " + texto2.ljust(largura_coluna - 1) + "║"
        print(linha)

    # Linha inferior
    if n_sequencia == "meio" or n_sequencia == "inicio":
        print("╠" + "═" * (largura_layout - 2) + "╣")
    else:
        print("╚" + "═" * (largura_layout - 2) + "╝")

# Exemplo de uso
textos_coluna1 = ["Coluna 1 - Linha 1", "Coluna 1 - Linha 2"]
textos_coluna2 = ["Coluna 2 - Linha 1", "Coluna 2 - Linha 2"]

def print_meio(titulo):
    print()
    print( " " * ((largura_layout // 2) - len(titulo) // 2)  + titulo)

def gerar_retangulo_com_titulo(textos, titulo):
    """
    Gera um retângulo com bordas e textos organizados dentro, incluindo um título.

    :param textos: Lista de strings para exibir dentro do retângulo.
    :param largura: Largura do retângulo.
    :param titulo: Texto do título a ser exibido na borda superior.
    """
    # Ajusta o título para caber na largura
    espaco_titulo = (largura_layout - len(titulo) - 4) // 2
    linha_titulo = "═" * espaco_titulo + " " + titulo + " " + "═" * espaco_titulo

    # Ajusta a linha se a largura do título for ímpar
    if len(linha_titulo) < largura_layout - 2:
        linha_titulo += "═"

    # Linha superior com título
    print()
    print("╔" + linha_titulo + "╗")

    # Linhas com textos
    for texto in textos:
        # Calcula o espaço em branco necessário para centralizar o texto
        espaco = (largura_layout - 2 - len(texto)) // 2
        print("║" + " " * espaco + texto + " " * (largura_layout - 2 - len(texto) - espaco) + "║")

    # Linha inferior
    print("╚" + "═" * (largura_layout - 2) + "╝")

# Exemplo de uso
