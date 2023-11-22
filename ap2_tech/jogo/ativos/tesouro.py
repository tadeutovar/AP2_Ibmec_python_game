
import random


class Tesouro:
    def __init__(self, limite):
        self.caractere = "X"
        self.posicao = [random.randint(1, limite - 1), random.randint(1, limite - 1)]
        
