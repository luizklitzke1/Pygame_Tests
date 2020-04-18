from general_functions import *

class Calendario():
    
    def __init__(self,ciclo=10,dia=1,mes=1,ano=1969):
        self.dia = 1
        self.dias = [
            "Segunda-Feira","Terça-Feira","Quarta-Feira","Quinta-Feira","Sexta-Feira",
            "Sábado","Domingo"
        ]
        self.dia_pos = 0
        self.mes = 1
        self.semana = 0
        self.meses = ["Janeiro","Fevereiro","Março","Abril","Maio","Junho",
                      "Julho","Agosto","Setembro","Outubro","Novembro","Dezembro"]
        self.ano = ano
    
        self.ciclo= ciclo
        self.ciclo_pos = ciclo
        
        self.lista_x = []
        
    #Atualização dos dados a cada frame
    def update(self):
        self.ciclo_pos -= 1
        
        if self.ciclo_pos == 0:
              
            if self.dia_pos == 6:
                self.dia_pos = 0
                self.semana += 1
            else:
                self.dia_pos += 1  
                
            if self.dia == 28:
                self.mes += 1
                self.dia = 1
                self.semana = 0
                self.lista_x = []
            else:
                self.dia += 1
            
            if self.mes == 13:
                self.ano += 1
                self.mes = 1
            
            self.ciclo_pos = self.ciclo
           
    #Representação visual do calendário na tela
    def rep_visual(self,screen,sw,sh):
        
        img_calend = draw_img(screen,"calend1.png",(swi(sw,.2),int(swi(sw,.2)*.853)),(swi(sw,.01),shi(sh,.54)))
        
        print(swi(sw,.2),int(swi(sw,.2)*.85))
        
        draw_text(self.meses[self.mes-1]+" - "+str(self.ano),preto,screen,x=swi(sw,.018),y=shi(sh,.565))
        
        x_dia=swi(sw,.0245) + swi(sw,.026)*self.dia_pos
        y_dia = shi(sh,.62)  + shi(sw,.022)*self.semana 
        
        draw_img(screen,"select.png",(swi(sw,.0198),shi(sh,.03)),(x_dia,y_dia))
        
        self.lista_x.append((x_dia,y_dia))

        for x in self.lista_x:
            draw_text("X",vermelho,screen,x=x[0],y=x[1], tamanho=swi(sw,.019))
        
        draw_text("Dia - "+str(self.dia),branco,screen,x=swi(sw,.020),y=shi(sh,.79))
        
    #Print dos valores atuais            
    def __repr__(self):
        return f""" {self.dias[self.dia_pos]} - Dia: {self.dia}\
               {self.meses[self.mes-1]} - Mês:  {self.mes}  Ano: {self.ano} """
      
               
