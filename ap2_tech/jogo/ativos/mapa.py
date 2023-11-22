class Mapa:
    def __init__(self, tamanho):
        self.tamanho = tamanho
        self.separacao = 6


    def desenhar(self, objetos):
        titulo = "»»————-MAPA————-««"
        print( " " * (((self.tamanho * (self.separacao + 1)) // 2) - len(titulo) // 2)  + titulo)
        for y in range(self.tamanho):
            for x in range(self.tamanho):
                objeto_encontrado = False
                for o in objetos:
                    if o.posicao == [x, y]:
                        self.printa(o.caractere)
                        objeto_encontrado = True
                        break
                if not objeto_encontrado:
                    self.printa(".")
            print()




    def printa(self, p):
        print(" " * (self.separacao // 2) + f"{p}" + " " * (self.separacao // 2), end="") 