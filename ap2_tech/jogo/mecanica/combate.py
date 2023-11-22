import random
import time
from jogo.ativos import item, mapa, tesouro, layout
class Combate:
    def __init__(self):
        self.critico = False
        
    def rodadas(self,p1, m):
        while True:
            acao = input("Insira o seu comando:").upper()
            if acao in ["I", "A", "D"]:

                

                d = 0 
                
                    
                if acao == "I":
                    p1.ver_mochila()
                    if not self.critico:
                        d = m.defendeu()
                    else:
                        time.sleep(2)
                    atitude_p1 = [f"{p1.nome} Usou a Mochila!"]
                    if d:
                        atitude_m = [f"{m.nome} Defendeu!","",""]
                        atitude_m.append(f"Valor:{d}")
                    elif not self.critico:
                        m.bater(p1, p1.defesa // 2, self.critico)
                        atitude_m = [f"{m.nome} Estunado!"]
                        atitude_m.append(f"Atacou pouco efetico")
                        atitude_m.append("")
                        atitude_m.append(f"Valor:{d}")
                    elif self.critico:
                        atitude_m = [f"{m.nome} Estunado!"]
                        atitude_m.append(f"Nenhuma ação...")
                        self.critico = False


                if acao == "D":
                    if not self.critico:
                        d = m.defendeu()
                    else:
                        time.sleep(2)
                    d_p1 = p1.defender()
                    atitude_p1 = [f"{p1.nome} Defendeu!","",""]
                    atitude_p1.append(f"valor:{d_p1}")
                    if d:
                        atitude_m = [f"{m.nome} Defendeu!","",""]
                        atitude_m.append(f"valor:{d}")
                    elif not self.critico:
                        if  random.randint(0, 1):    
                            self.critico = True                      
                            layout.print_meio(f"✶ {m.nome} atacou, mas você Bloqueia Parte do Ataque!")
                            layout.print_meio("Zz  Inimigo atordoado, não joga a proxima rodada...")
                            time.sleep(1)
                            dano = m.bater(p1, d_p1, self.critico)
                            atitude_m = [f"{m.nome} Atacou com","pouca efetividade.."]
                            atitude_m.append("")
                            atitude_m.append(f"Efetividade:{dano}")
                        else:                         
                            dano = m.bater(p1, d_p1, False)
                            atitude_m = [f"{m.nome} Atacou!"]
                            atitude_m.append("")
                            atitude_m.append("")
                            atitude_m.append(f"Efetividade:{dano}")
                    elif self.critico:
                        atitude_m = [f"{m.nome} Estunado!"]
                        atitude_m.append(f"Nenhuma ação...")
                        self.critico = False
                        
                        


                elif acao == "A":
                    if not self.critico:
                        d = m.defendeu()
                    else:
                        time.sleep(2)

                    dano = p1.bater(m, d)
                    atitude_p1 = [f"{p1.nome} Atacou!"]
                    atitude_p1.append("")
                    atitude_p1.append(f"Efetividade:{dano}")
                    if not self.critico and d:
                        atitude_m = [f"{m.nome} Defendeu!"]
                        atitude_m.append("")
                        atitude_m.append(f"Valor:{d}")
                    elif self.critico:
                        atitude_m = [f"{m.nome} Atordoado!"]
                        atitude_m.append(f"Nenhuma ação...")
                        self.critico = False
                    else:
                        m.bater(p1, 0, self.critico)
                        atitude_m = [f"{m.nome} Atacou!"]
                        atitude_m.append("")
                        atitude_m.append(f"Efetividade:{dano}")
                        

                    
                    
                    
                break
            else: print("Comando não reconhecido")
        
        layout.gera_layout(atitude_p1,atitude_m, " ◊════╡■■■■■■■■■■■■► ")

        

    def combate (self,p1, m):
        rodada = 0
        layout.gerar_retangulo_com_titulo(["Combate!", f"Um {m.nome} Apareceu em seu caminho"], " ◊════╡▮▮▮▮▮▮▮▮▮▮▮▮ ◤ ")
        while True:
            
            layout.gera_layout(p1.status(),m.status(),f" Rodada: {rodada} ","inicio")
            layout.gera_layout(["Opções de ação:","➣ (A) Atacar","➣ (D) Defender", "➣ (I) Ver mochila"],[],"","final")
            self.rodadas(p1,m)
            rodada += 1
            if p1.vida_atual <= 0:
                layout.gerar_retangulo_com_titulo(p1.status(), " ❰❮ ⛒ DERROTA ⛒ ❯❱")
                return False
            if m.vida_atual <= 0:
                layout.gerar_retangulo_com_titulo(p1.status(), " ❰❮ ◈ VITÓRIA ◈ ❯❱")
                p1.pontos += m.vida_maxima
                return True
            
            
