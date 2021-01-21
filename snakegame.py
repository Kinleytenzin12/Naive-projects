# import pygame #snake game
# import sys #has the exit function
# import random #place food in random position. 
# import time # to pause the screen

import pygame, sys,	random, time

#(6,0)
check_error = pygame.init() #initilises the pygame
if check_error[1] > 0:
	print('error')
	sys.exit(-1)
else:
	print('successfuly')

#Play surface
playSurface = pygame.display.set_mode((740, 460))
# set.mode() is a inbuilt function. set mode only accept one, thus you make it one element by putting into one bracket.

pygame.display.set_caption('Snake game')
#to change the caption.its a inbuilt funcion.

#time.sleep(5) #time.sleep is to pause for five second

#Color
#three color (R,G,B) = (250,0,0)means green and blue is zero
red = pygame.Color(255,0,0)  #gameover
green = pygame.Color(0,255,0) #snake
black = pygame.Color(0,0,0) #score
white = pygame.Color(255,255,255) #background
brown = pygame.Color(165,45,42) #food

# FPS - frames per second
fpsController = pygame.time.Clock()

#important variable
snakePos = [100,50] #snake postion in x- left and right and y - up and down (x=100). dont exceed set_mode
snakeBody = [[100,50],[90,50],[80,50]] #to add list of list add comma

foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10] #x and y coordinates 
#random range

foodSpawn = True

direction ="RIGHT" 
changeto = direction

score = 0

#game over function

def gameOver():
	myFont = pygame.font.SysFont('manaco', 72) #specify name of the font and size of font
	GOsurf = myFont.render('GOODBYE 2020, I LOVE YOU', True, red) 
#require three things, text, boolean, color, and background(optional by default it wil be none)

	GOrect = GOsurf.get_rect() #rectangle component  of the gamer over 
	GOrect.midtop = (360, 115) 
#placing on the surface. specify x and y coordinate. screen size 720/2    
	playSurface.blit(GOsurf, GOrect)
#put in the surface
	time.sleep(10)
	showScore(2)
	pygame.display.flip()
#update the screen. update() = flip()
	pygame.quit() #pygame exit
	sys.exit() #console exit

#score
def showScore(choice=1):
	sFont = pygame.font.SysFont('manaco', 24)
	Ssurf = sFont.render('Score : {0}'.format(score), True, red)
	Srect = Ssurf.get_rect()
	if choice ==1:
		Srect.midtop = (80, 10)
	else:
		Srect.midtop = (360, 120)
		
	playSurface.blit(Ssurf, Srect)
# Main logic of the game.

#for looping fps infinitly

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_RIGHT or event.key == ord('d'):
				changeto = 'RIGHT'
			if event.key == pygame.K_LEFT or event.key == ord('a'): 
				changeto = 'LEFT'
			if event.key == pygame.K_UP or event.key == ord('w'): 
				changeto = 'UP'
			if event.key == pygame.K_DOWN or event.key == ord('s'): 
				changeto = 'DOWN'
			if event.key == pygame.K_ESCAPE:
				pygame.event.post(pygame.event.Event(pygame.QUIT))
			#w
			#asd -- d is right, a is left
			
#validation of direction. if direction if up you cannot go up

	if changeto =='RIGHT' and not direction =='LEFT':
		direction = 'RIGHT'
	if changeto =='LEFT' and not direction =='RIGHT':
		direction = 'LEFT'
	if changeto =='UP' and not direction =='DOWN':
		direction = 'UP'
	if changeto =='DOWN' and not direction =='UP':
		direction = 'DOWN'

	if direction == 'RIGHT':
		snakePos[0] += 10
	if direction == 'LEFT':
		snakePos[0] -= 10
	if direction == 'UP':
		snakePos[1] -= 10
	if direction == 'DOWN':
		snakePos[1] +=10


	# body mechanism

	snakeBody.insert(0, list(snakePos))
	if snakePos[0] == foodPos[0] and snakePos[1] == foodPos[1]:
		score += 1
		foodSpawn = False

	else: 
		snakeBody.pop()

	if foodSpawn == False:
		foodPos = [random.randrange(1,72)*10, random.randrange(1,46)*10]
	foodSpawn = True

	#background

	playSurface.fill(white)
	
	#Draw Snake
	for pos in snakeBody:
		pygame.draw.rect(playSurface,green,pygame.Rect(pos[0], pos[1],10,10))

	#fo0d
	pygame.draw.rect(playSurface,brown,pygame.Rect(foodPos[0],foodPos[1],10,10))
	
	if snakePos[0] > 710 or snakePos[0]<0:
		gameOver()
	if snakePos[1] > 450 or snakePos[1] < 0:
		gameOver()

	for block in snakeBody[1:]:
		if snakePos[0]==block[0] and snakePos[1]==block[1]:
			gameOver()


	showScore()
	pygame.display.flip() #to update the code
	fpsController.tick(23) #27 per second
























