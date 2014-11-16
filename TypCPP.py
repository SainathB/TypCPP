
import sys,pygame
from pygame.locals import *
import random
def pop_out(x):
	str=""
	for i in range (len(x)-1):
		str+=(x[i]) 
	return str	
class stringob:
	def __init__(self,item,x,y,z):
		self.item=item
		self.x=x
		self.y=y
		self.z=z
		
pygame.init()
pygame.display.set_caption("TypCPP")
size=(width,height)=(700,550)
red=230,0,0
myFont=pygame.font.SysFont("AndaleMono.ttf",30)
label=myFont.render("PLAY",1,(0,0,160))
scorelabel=myFont.render("SCORE:",1,(0,0,255))
typelabel=myFont.render("TYPE:",1,(0,0,255))
yourscorelabel=myFont.render("YOUR FINAL SCORE IS..",1,(0,0,255))
chances_left_label=myFont.render("CHANCES LEFT:",1,(0,0,255))
rect=label.get_rect()
screen=pygame.display.set_mode(size)
score=0
chances_left=65;
mainstr=""
keywords=["alignas","alignof","and","and_eq","asm","auto","bitand","bitor","bool","break","case","catch","char","char16_t","char32_t","class","compl","const","constexpr" ,"const_cast","continue","decltype","default","delete","do","double","dynamic_cast","else","enum","explicit","export","extern","false","float","for","friend","goto","if","inline","int","long","mutable","namespace","new","noexcept","not","not_eq","nullptr","operator","or","or_eq","private","protected","public","register","reinterpret_cast","return","short","signed","sizeof","static","static_assert","static_cast","struct","switch","template","this","thread_local","throw","true","try","typedef","typeid","typename","union","unsigned","using","virtual","void","volatile","wchar_t","while","xor","xor_eq"];
no_of_keywords=len(keywords)
flag=0
prev=pygame.time.get_ticks()
while flag==0:
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		if event.type==pygame.KEYDOWN:
                        if event.key == pygame.K_ESCAPE:
                                sys.exit()
		if event.type==pygame.MOUSEBUTTONDOWN:
			l=event
			(x,y)=l.pos
			recw=rect.width
			rech=rect.height
			
			if(x>=310 and x<=310+recw and y>=230 and y<=230+rech):
				flag=1
				print x,y
	screen.fill((47, 248, 79))
	screen.blit(label,(310,230));		
	pygame.display.flip()
	
queue=[]
randomnumber=random.randint(0,83)
item=myFont.render(keywords[randomnumber],1,(255,0,0))
randx=random.randint(1,600)
queue.append(stringob(item,x,40,keywords[randomnumber]))
speed=0.05
newgentime=1000
prev1=pygame.time.get_ticks()
prev2=pygame.time.get_ticks()		
while(len(queue) and chances_left>0):
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
		elif event.type==KEYDOWN:
			inkey=event.key
                        if inkey == pygame.K_ESCAPE:
                                sys.exit()
			elif inkey==K_RETURN:
				for ppp in queue:
					if ppp.z==mainstr:
						score+=3
						queue.remove(ppp)	
				mainstr=""
			elif inkey==K_BACKSPACE:
				if len(mainstr)>0:
					mainstr=pop_out(mainstr)
			elif inkey==K_MINUS:
				mainstr+="_"
			elif inkey<=127:
				mainstr+=(chr(inkey))					
	if queue[0].y>=500:
		queue.pop(0)
		if chances_left>0:
		   chances_left-=1		
	present1=pygame.time.get_ticks()
	timeelapsed1=present1-prev1
	prev1=present1
	for i in range (len(queue)):
		queue[i].y=queue[i].y+timeelapsed1*speed
	present2=pygame.time.get_ticks()
	if(present2-prev2>=newgentime):
		randomnumber=random.randint(0,83)
		item=myFont.render(keywords[randomnumber],1,(255,0,0))
		randx=random.randint(1,600)
		queue.append(stringob(item,randx,40,keywords[randomnumber]))
		prev2=present2
		newgentime=0.999 * newgentime
	screen.fill((255,255,255))	
	for i in range (len(queue)):
		screen.blit(queue[i].item,(queue[i].x,queue[i].y))
	pygame.draw.rect(screen,(0,255,0),(0,0,700,30),3)
	screen.blit(scorelabel,(5,5))
	screen.blit(myFont.render("%r"%(score),1,(39, 38, 36)),(105,5))
	screen.blit(chances_left_label,(400,5))
	screen.blit(myFont.render("%r"%(chances_left),1,(39, 38, 36)),(605,5))
	pygame.draw.rect(screen,(0,255,0),(0,515,700,30),3)
	screen.blit(typelabel,(5,520))		
	screen.blit(myFont.render(mainstr,1,(39, 38, 36)),(105,520))
	pygame.display.flip()
while 1:
	
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			sys.exit()
	screen.fill((47, 248, 79))
	screen.blit(yourscorelabel,(260,230));
	screen.blit(myFont.render("%r"%(score),1,(39, 38, 36)),(360,270))		
	pygame.display.flip()



