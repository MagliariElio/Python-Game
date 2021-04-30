import pygame
import sys
import time
import random

width = 500
height = 500
rows = 20

#################################     

def snake(screen,snakeList):
    
    for value in snakeList:
        pygame.draw.rect(screen,(255,0,0),((value[0])+2,(value[1])+2,(width//rows)-3,(height//rows)-3))
    pygame.display.update()

#################################  

def Message(screen,string,color,x,y,size,Bold):

    font = pygame.font.SysFont("Arial",size,Bold)
    text = font.render(string,True,color)
    screen.blit(text,[x,y])
    pygame.display.update()

#################################  

def drawGrid(screen):
    distx = width // rows
    disty = height // rows
    x = 0
    y = 0
    
    for n in range(width):
        pygame.draw.line(screen,(255,128,0),(x,0),(x,height))
        x += distx 

    for m in range(height):
        pygame.draw.line(screen,(255,128,0),(0,y),(width,y))
        y += disty

    pygame.display.update()

#################################     
    
def edge(screen,posx,posy,body,minute,second,TenSecond,Increment):

      if posx < 0 or posx >= width or posy < 0 or posy >= height:
          screen.fill((0,0,0))
          pygame.mixer.Sound.stop(Increment)
          death = ["CENTODICIOTTO.wav","Baby_Crying.wav"]
          choose = random.randrange(0,len(death))
          dead_1 =  pygame.mixer.Sound("Strong_Punch.wav")
          dead_2 = pygame.mixer.Sound(death[choose])
          pygame.mixer.Sound.play(dead_1)
          pygame.mixer.Sound.play(dead_2)
          Message(screen,"Game Over",(255,0,0),130,190,60,True)
          print("Score:", len(body))
          TIME_minute = str(minute)
          TIME_second = str(second)
          TIME_TenSecond = str(TenSecond)
          print("Time:",TIME_minute + ":" + TIME_second + ":" + TIME_TenSecond)
          if death[choose] == "Baby_Crying.wav":
              time.sleep(4.2)
          elif death[choose] == "CENTODICIOTTO.wav":
              time.sleep(6)
          pygame.mixer.Sound.stop(dead_2)
          
          GAME()          
  
      pygame.display.update()

#################################        

def Snack(screen,posxSnack,posySnack):
    color = (random.randrange(255),random.randrange(255),random.randrange(255))
    pygame.draw.rect(screen,color,(posxSnack+2,posySnack+2,(width//rows)-3,(height//rows)-3))    

#################################  

def GAME():
    
    pygame.font.init()
    pygame.mixer.init()
    
    global width, height
    screen = pygame.display.set_mode((width,height))
    pygame.display.set_caption("Snake")

    
    clock = pygame.time.Clock()
    FPS = 8

    distx = width // rows
    disty = height // rows

    posxSnack = random.randrange(0,width,distx)
    posySnack = random.randrange(0,height,disty)
    
    posx = width // 2
    posy = height // 2

    diff = 1
    minute = 0
    second = 0
    TenSecond = 0
    Audio_again = 1
    Increment = pygame.mixer.Sound("Aumento_Difficolta'.wav")

    body = []
    snakeList = 1

    x = 0
    y = 0
  
    run = True
    while run:
            
       for event in pygame.event.get():
              
         if event.type == pygame.QUIT:
               pygame.quit()
               sys.exit()

         events = pygame.key.get_pressed()

         for key in events:
              if events[pygame.K_UP]:
                     y = -disty
                     x = 0
              elif events[pygame.K_DOWN]:
                     y = disty
                     x = 0
              elif events[pygame.K_RIGHT]:
                     x = distx
                     y = 0
              elif events[pygame.K_LEFT]:
                     x = -distx
                     y = 0

       posx += x
       posy += y
       head = [posx,posy]
       body.append(head)


       
       if body[0] in body[1:] and snakeList > 1:           # controlla se lo snake non si morde
          screen.fill((0,0,0))
          dead_3 = pygame.mixer.Sound("Porcoschifo.wav")
          pygame.mixer.Sound.play(dead_3)
          Message(screen,"Game Over",(255,0,0),130,190,60,True)
          print("Score:", len(body))
          TIME_minute = str(minute)
          TIME_second = str(second)
          TIME_TenSecond = str(TenSecond)
          print("Time:",TIME_minute + ":" + TIME_second + ":" + TIME_TenSecond)
          time.sleep(5)
          GAME()          
          pygame.display.update()
          

       if len(body) > snakeList:         # gestione del corpo dello snake
           del body[0]
           

       if len(body) == FPS + diff:       # aumento della difficoltà
           FPS += 2
           diff += 9
           Audio_again += 1
           print("Score:", len(body))
           if Audio_again == 3:
              pygame.mixer.Sound.play(Increment)
                  

       if posx == posxSnack and posy == posySnack:        # aggiunge uno snack appena lo snake ne mangia uno
            eat = pygame.mixer.Sound("eat.wav")
            pygame.mixer.Sound.play(eat)
            add = pygame.draw.rect(screen,(255,255,0),(posx,posy,width//rows,height//rows))
            body.append(add)
            posxSnack = random.randrange(0,width,distx)
            posySnack = random.randrange(0,height,disty)
            snakeList += 1
            randomPos = False
            while randomPos == False:                                 # controlla che lo snack non spawna sul corpo
              if posxSnack in body and posySnack in body:
                  posxSnack = random.randrange(0,width,distx)
                  posySnack = random.randrange(0,height,disty)
              else:
                  randomPos = True

           
       screen.fill((0,0,0))    # colora sfondo
       drawGrid(screen)        # disegna griglia


       TenSecond += 1          # contatore del tempo da inizio partita
       if TenSecond == 8:        # un decimo di secondo 
           TenSecond = 0
           second += 1
       if second == 60:
           second = 0
           minute += 1 

           
       snake(screen,body)   # snake        

       Snack(screen,posxSnack,posySnack)  # aggiunge gli Snack

       edge(screen,posx,posy,body,minute,second,TenSecond,Increment)   # controlla che non si va fuori i margini
           
       pygame.display.update() # aggiorna lo schermo
       
       clock.tick(FPS) # velocita' frame al secondo 

#################################        
      

              



GAME()

       
            

    
