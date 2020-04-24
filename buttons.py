import pygame
import glob 

pygame.init()


#Módulo com as classes gerais utilizadas por todo o código

from general_functions import *

class Button():
    def __init__(self,color,x,y,width,height,text,text_rus=None,text_size=None,text_color=branco):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
        self.text_rus = text_rus
        self.text_size = text_size
        self.hover = False

    #Desenha o botão na tela
    def draw(self,screen,rus=False,outline=None):
        
        if outline:
            pygame.draw.rect(screen, outline, (self.x-4,self.y-4,self.width+8,self.height+8),0)
            
        rect = pygame.draw.rect(screen, self.color, (self.x,self.y,self.width,self.height),0)
        
        if rus:
            draw_text(self.text_rus,preto,screen,center=rect.center,tamanho=self.text_size)
        else:
            draw_text(self.text,preto,screen,center=rect.center,tamanho=self.text_size)
            

    #Testa colisão 
    def isOver(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                if self.hover == False:
                    btn2.play()
                    self.hover = True
                return True
        self.hover = False
        return False
    
#Setup separado dos botões utilizados na tela de seleção inicial
def setup_botoes_inicial(sh,sw):
    margem_x = swi(sw,.03)
    w_botao = swi(sw,.15)
    h_botao = shi(sh,.05)
    btn_Trofimovsk = Button(branco,margem_x,shi(sh,.2),w_botao,h_botao,"Trofimovsk","Трофимовск")
    btn_Solovetsky = Button(branco,margem_x,shi(sh,.3),w_botao,h_botao,"Solovetsky","Соловетскы")
    btn_Norilsk = Button(branco,margem_x,shi(sh,.4),w_botao,h_botao,"Norilsk","Норилск")
    btn_Sevvostlag = Button(branco,margem_x,shi(sh,.5),w_botao,h_botao,"Sevvostlag","Севвостлаг")
    btn_Pechorlag = Button(branco,margem_x,shi(sh,.6),w_botao,h_botao,"Pechorlag","Печорлаг")
    btn_Karlag = Button(branco,margem_x,shi(sh,.7),w_botao,h_botao,"Karlag","Карлаг")
    btn_Altayskiy = Button(branco,margem_x,shi(sh,.8),w_botao,h_botao,"Altayskiy","Алтаыскиы")
    
    return [btn_Trofimovsk,btn_Solovetsky,btn_Norilsk,btn_Sevvostlag,btn_Pechorlag,btn_Karlag,btn_Altayskiy]

def setup_botoes_game(sh,sw):

    margem_x = swi(sw,.015)
    w_botao = swi(sw,.17)
    h_botao = shi(sh,.08)
    btn_status= Button(branco,margem_x,shi(sh,.15)-8,w_botao,h_botao,"Status","Статус")
    btn_recursos = Button(branco,margem_x,shi(sh,.25)-8,w_botao,h_botao,"Recursos","Рецурсос")
    btn_upgrades= Button(branco,margem_x,shi(sh,.35)-8,w_botao,h_botao,"Upgrades","Упградес")
    
    lista_btns = [btn_status,btn_recursos,btn_upgrades]
    
    return lista_btns

def setup_botoes_vel(sh,sw):
    margem_x = swi(sw,.76)
    margem_y = shi(sh,.85)
    w_botao = swi(sw,.07)
    h_botao = shi(sh,.08)
    btn_1x = Button(branco,margem_x,margem_y,w_botao,h_botao,"1x",text_size=swi(sw,.013))
    btn_2x = Button(branco,margem_x+w_botao+10,margem_y,w_botao,h_botao,"2x",text_size=swi(sw,.013))
    btn_5x = Button(branco,margem_x+w_botao*2+20,margem_y,w_botao,h_botao,"5x",text_size=swi(sw,.013))
    
    lista_btns = [btn_1x,btn_2x,btn_5x]
    
    return lista_btns

def setup_botoes_pause(sh,sw):
    margem_x = swi(sw,.31)
    margem_y = shi(sh,.3)
    w_botao = swi(sw,.18)
    h_botao = shi(sh,.1)
    tamanho = swi(sw,.012)
    btn_resume = Button(branco,margem_x,margem_y,w_botao,h_botao,"Resume",text_size=tamanho)
    btn_save = Button(branco,margem_x+w_botao+20,margem_y,w_botao,h_botao,"Salvar",text_size=tamanho)
    btn_opt = Button(branco,margem_x,margem_y+h_botao*1+20,w_botao,h_botao,"Opções",text_size=tamanho)
    btn_menu = Button(branco,margem_x+w_botao+20,margem_y+h_botao*1+20,w_botao,h_botao,"Menu inicial",text_size=tamanho)
    btn_quit = Button(branco,swi(sw,.4),margem_y+int(h_botao*2.5),w_botao,h_botao,"Sair do jogo",text_size=tamanho)
    
    lista_btns = [btn_resume,btn_save,btn_opt,btn_menu,btn_quit]
    
    return lista_btns

def setup_botoes_res(sh,sw):
    margem_x = swi(sw,.07)
    margem_y = shi(sh,.38)
    w_botao = swi(sw,.13)
    h_botao = shi(sh,.08)
    btn_1 = Button(branco,margem_x,margem_y,w_botao,h_botao,"852x480",text_size=swi(sw,.013))
    btn_2 = Button(branco,margem_x+w_botao+10,margem_y,w_botao,h_botao,"1280x720",text_size=swi(sw,.013))
    btn_3 = Button(branco,margem_x+w_botao*2+20,margem_y,w_botao,h_botao,"1365x768",text_size=swi(sw,.013))
    btn_4 = Button(branco,margem_x+w_botao*3+30,margem_y,w_botao,h_botao,"1600x900",text_size=swi(sw,.013))
    btn_5 = Button(branco,margem_x+w_botao*4+40,margem_y,w_botao,h_botao,"1920x1080",text_size=swi(sw,.013))

    lista_btns = [btn_1,btn_2,btn_3,btn_4,btn_5]
    
    return lista_btns