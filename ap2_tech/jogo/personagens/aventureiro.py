import random
from jogo.ativos import layout

class Aventureiro:
    def __init__(self, nome):
        self.caractere = "@"
        self.mochila = []
        self.nome = nome
        self.posicao = [0,0]
        self.vida_maxima = random.randint(100, 120)
        self.forca = random.randint(10, 18)
        self.defesa = random.randint(10, 18)
        self.vida_atual = self.vida_maxima
        self.pontos = 0

    def receber_efeito(self, tipo, intensidade):
        if tipo == 'vida':
            vida_anterior = self.vida_atual
            self.vida_atual = min(self.vida_atual + (20 * intensidade), self.vida_maxima)
            layout.print_meio(f"{self.nome} recuperou {20 * intensidade} pontos de vida.")
            layout.print_meio(f"{vida_anterior}/{self.vida_maxima}  ➣  {self.vida_atual}/{self.vida_maxima}")
        elif tipo == 'forca':
            self.forca += intensidade
            layout.print_meio(f"{self.nome} aumentou a força em {intensidade}.")
            layout.print_meio(f"{self.forca - intensidade}  ➣  {self.forca}")
        elif tipo == 'defesa':
            self.defesa += intensidade
            layout.print_meio(f"{self.nome} aumentou a defesa em {intensidade}.")
            layout.print_meio(f"{self.defesa - intensidade}  ➣  {self.defesa}")



    def receber_dano(self, valor,defesa):
        dano = valor - min(defesa, valor)
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0
        return dano

    def bater(self, alvo, defesa):
        return alvo.receber_dano(self.forca,defesa)

    def defender(self):
        c = random.randint(0, 2)
        if c == 0 :
            return self.defesa // 2
        else: return self.defesa
        
    def status(self):
        return [self.nome,f"Vida: {self.vida_atual}/{self.vida_maxima}",f"Força: {self.forca}",f"Defesa: {self.defesa}"]
    
    def ver_mochila(self, n_sequencia = ""):
        itens1 = []
        itens2 = []
        if self.mochila:
            t = len(self.mochila) - 1
            for i, e in enumerate(self.mochila):
                if i <= t // 2:
                    itens1.append(f"{i + 1} ➣ {e.nome} nível {e.intensidade}")
                else: itens2.append(f"{i + 1} ➣ {e.nome} nível {e.intensidade}")
            
            layout.gera_layout(itens1,itens2," Mochila ",n_sequencia)
            while True:
                escolha = int(input("Escolha uma das possoes por indice (0 - cancela a Escolha):")) - 1
                if escolha == -1:
                    print()
                    print("Ação cancelada")
                    break
                if escolha >= 0 and escolha <= t:
                    for i, e in enumerate(self.mochila):
                        if i == escolha:
                            self.mochila.remove(e)
                            self.receber_efeito(e.tipo, e.intensidade)
                    break
                else: 
                    print()
                    print("Você não possue esse item... Tente Novamente")
        else : layout.gerar_retangulo_com_titulo(["Você ainda não encontrou nenhum item"]," Mochila " )