import random

from jogo.ativos import item, mapa, tesouro, layout
from jogo.mecanica import combate
from jogo.personagens import aventureiro, monstro


    


def movimentar(p1, dir, mapa):
    p = p1.posicao
    if dir == "W":
        posicao = [p[0], p[1] - 1]
    elif dir == "A":
        posicao = [p[0] - 1, p[1]]
    elif dir == "S":
        posicao = [p[0], p[1] + 1]
    else:
        posicao = [p[0] + 1, p[1]]

    # Verificar se a nova posição é válida (dentro dos limites do mapa)
    if 0 <= posicao[0] < mapa.tamanho and 0 <= posicao[1] < mapa.tamanho:
        p1.posicao = posicao


        # evento = random.choices(["nada", "item", "monstro"],[0.4,0.2,0.4], k=1)[0]
        # if evento == "item":
        #     itens = [c1,c2,f1,f2,d1]
        #     percent = []
        #     for i in itens:
        #         percent.append( i.porcentagem)

            
        #     item = random.choices(itens, percent, k=1)[0]

        #     p1.mochila.append(item)
        #     print(item.nome)
        #     pass
        # elif evento == "monstro":
        #     m = monstro.Monstro("BaltaZar")
        #     combate.iniciar_combate(p1,m)
        #     pass
        
        return True
    else:
        print("Você não pode se mover para lá.")
        return True
    
# Definição da classe Item já fornecida

# Criação dos itens
pocao_forca_1 = item.Item("Poção de Força", "forca", 1)
pocao_forca_2 = item.Item("Poção de Força", "forca", 2)
pocao_vida_1 = item.Item("Poção de Vida", "vida", 1)
pocao_vida_2 = item.Item("Poção de Vida", "vida", 2)
pocao_defesa_1 = item.Item("Poção de Defesa", "defesa", 1)

monstros = []

def random_efeitos(p1):
    opcoes = ["nada", "monstro", "item"]
    probabilidades = [0.4, 0.4, 0.2]

    escolha = random.choices(opcoes, probabilidades, k=1)[0]

    

    # Lista de itens e suas probabilidades
    itens = [pocao_forca_1, pocao_forca_2, pocao_vida_1, pocao_vida_2, pocao_defesa_1]
    probabilidades = [0.10, 0.05, 0.50, 0.30, 0.05]  # 10%, 5%, 50%, 30%, 5%

    # Escolhendo um item com base nas probabilidades
    item_escolhido = random.choices(itens, probabilidades, k=1)[0]

    # Exemplo de uso
    # Suponha que temos um objeto 'aventureiro' que pode usar o item
    # item_escolhido.usar(aventureiro)
    if escolha == opcoes[1]:
        m = monstro.Monstro("Monstro", p1.posicao)
        partida = combate.Combate()
        comb = partida.combate(p1, m)
        if comb:
            monstros.append(m)
        return comb
    if escolha == opcoes[2]:

        e = random.choices(itens, probabilidades, k=1)[0]
        p1.mochila.append(e)
        layout.print_meio(f"-[ Você encontrou {e.nome} nível {e.intensidade} ]-")
    return True
    

def jogo():
    map = mapa.Mapa(10)
    print()
    nome = input("Deseja buscar um tesouro? Primeiro, informe seu nome: ")
    p1 = aventureiro.Aventureiro(nome)
    layout.gerar_retangulo_com_titulo([f"Saudações, {nome}! Boa sorte!"],">> Caça ao Tesouro <<")
    print()
   

    tes = tesouro.Tesouro(map.tamanho)
    map.desenhar([p1, tes])

    while True:
        
        op = input("Insira o seu comando: ").upper()
        if op == "Q":
            print("Já correndo?")
            break

        if op == "T":
            p1.ver_atributos()
        elif op == "I":
            p1.ver_mochila()
            map.desenhar([p1, tes] + monstros)
        elif op in ["W", "A", "S", "D"]:
            
            if movimentar(p1, op, map):
                if not random_efeitos(p1):
                    layout.gerar_retangulo_com_titulo(["Não foi dessa vez.."]," X Game Over X " )
                    break
                map.desenhar([p1, tes] + monstros)
            else:
                print("Game Over...")
                break
        else:
            print(f"{p1.nome}, não conheço essa! Tente novamente!")

        if p1.posicao == tes.posicao:
            layout.gerar_retangulo_com_titulo([f"Parabéns, {nome}!  Você encontrou o tesouro!",f"{len(monstros)} Monstros derrotados ✟", f"Com total de {p1.pontos}"],"☆ Vitória ☆")
            break
