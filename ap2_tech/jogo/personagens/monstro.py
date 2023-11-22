import random
import time
from jogo.ativos import item, mapa, tesouro, layout

class Monstro:
    def __init__(self, nome,posicao):
        self.caractere = "✟"
        self.nome = nome
        self.posicao = posicao
        self.vida_maxima = random.randint(10, 100)
        self.vida_atual = self.vida_maxima
        self.forca = random.randint(5, 25)
        self.defesa = random.randint(5, 10)


    def receber_dano(self, valor,defesa):
        dano = valor - min(defesa, valor)
        self.vida_atual -= dano
        if self.vida_atual < 0:
            self.vida_atual = 0
        return dano
        
            
    def bater(self, alvo,defesa, critico):
        if critico:
            return alvo.receber_dano(self.forca // 2, defesa)
        else: return alvo.receber_dano(self.forca,defesa)
        

    def defender(self):
        c = random.randint(0, 2)
        if c == 0 :
            return 1
        elif c == 2 :
            return self.defesa // 2
        else: return self.defesa

    
    def status(self):
        return [self.nome,f"Vida> {self.vida_atual}/{self.vida_maxima}",f"Força: {self.forca}",f"Defesa: {self.defesa}"]
    
    def defendeu(self):
        layout.print_meio("↻  Inimigo esta tomando uma Atitude...")
        time.sleep(2)
        c = random.randint(0, 1)
        if c == 1:
            return  self.defender()
        return 0

