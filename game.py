import pygame, sys
import time
import math
from config import *
t0=time.time()
clock=pygame.time.Clock()

pygame.init()
screenwidth=900
screenheight=530
screen=pygame.display.set_mode((screenwidth,screenheight))

width=30
height=30

player1=pygame.image.load("./images/cartoon.png")
player1=pygame.transform.scale(player1,(40,40))
player2=pygame.image.load("./images/superhero.png")
player2=pygame.transform.scale(player2,(40,40))
#block=(245,160,66)
#pos=(252,78,3)
#screencol=(66,185,245)

ob1=pygame.image.load("./images/dev1.png")
ob1=pygame.transform.scale(ob1,(50,50))
ob2=pygame.image.load("./images/dev2.png")
ob2=pygame.transform.scale(ob2,(50,50))
ob3=pygame.image.load("./images/dev3.png")
ob3=pygame.transform.scale(ob3,(50,50))

boat=pygame.image.load("./images/boat.png")
boat=pygame.transform.scale(boat,(40,40))

#player position
startxp=500
startyp=490
endxp=500
endyp=-5
x=startxp
y=startyp
val =10
jump=False
jumpcount=10

bs1=800
speed1=100
speed2=100
bs2=0
bs3=450
bs4=50
bs5=850

bl1=1
bl2=1
bl3=1
bl4=1
bl5=1

br1=0
br2=0
br3=0
br4=0
br5=0

pl=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
ps="points: "
pn=0


p=0
player=player1
#text
#black=(0,0,0)
#yellow=(245,236,66)
s='Start'
e='End'


#win
ct=0
pt1=0
pt2=0
s1=0
s2=0

c1=(66,185,245)
timer=pygame.font.Font(f2,27)
while 1:
	pygame.time.delay(100)
	t1=time.time()
	dt=t1-t0
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			pygame.quit()
			exit(0)
	#f=open("config.txt","a")
	screen.fill(screencol)
	screen.blit(boat,(bs1,40))
	screen.blit(boat,(bs2,140))
	screen.blit(boat,(bs3,240))
	screen.blit(boat,(bs4,340))
	screen.blit(boat,(bs5,440))

	pygame.draw.rect(screen,block,(0,0,900,30))
	pygame.draw.rect(screen,block,(0,100,900,30))
	pygame.draw.rect(screen,block,(0,200,900,30))
	pygame.draw.rect(screen,block,(0,300,900,30))
	pygame.draw.rect(screen,block,(0,400,900,30))
	pygame.draw.rect(screen,block,(0,500,900,30))
	pygame.draw.rect(screen,pos,(490,500,60,30))
	pygame.draw.rect(screen,pos,(490,0,60,30))

	screen.blit(ob2,(30,90))	#6
	screen.blit(ob3,(30,290))	#3
	screen.blit(ob2,(400,190))	#5
	screen.blit(ob3,(600,390))	#2
	screen.blit(ob1,(350,-10))	#9
	screen.blit(ob2,(150,485))   #1
	screen.blit(ob3,(200,90))	#7
	screen.blit(ob3,(800,-10))	#10
	screen.blit(ob2,(800,290))	#4
	screen.blit(ob1,(620,90))	#8
	font = pygame.font.Font(f1, 25)
	text = font.render(s, True, black, yellow)
	text2 = font.render(e,True,black,yellow)
	textRect = text.get_rect()
	textRect2=text2.get_rect()
	po=font.render(ps,True,black,yellow)
	porect=po.get_rect()
	porect.center=(70,13)

	pn=5*(pl[0]+pl[1]+pl[2]+pl[3]+pl[4]+pl[5]+pl[6]+pl[7]+pl[8]+pl[9])+10*(pl[10]+pl[11]+pl[12]+pl[13]+pl[14])
	ps="Points: "+str(pn)

	dts=math.floor(dt)
	mi=dts//60
	sec=dts%60
	tim=str(mi)+":"+str(sec)

	textt=timer.render(tim,True,black)
	textpos=textt.get_rect()
	textpos.center=(850,520)
	screen.blit(textt,textpos)

	#print(dts)

	"""while dts<4:
		fontx = pygame.font.Font(f1, 30)
		msg=fontx.render(msg,True,black,yellow)
		msgpos=msg.get_rect()
		msgpos.center=(500,400)
		screen.blit(msg,msgpos)"""



	def fail():
		fontx = pygame.font.Font(f1, 30)
		msg=fontx.render(fl,True,black,yellow)
		msgpos=msg.get_rect()
		msgpos.center=(500,400)
		#screen.fill(screencol)
		screen.blit(msg,msgpos)
		pygame.time.delay(100)


	def succ():
		fontx = pygame.font.Font(f1, 30)
		msg=fontx.render(suc,True,black,yellow)
		msgpos=msg.get_rect()
		msgpos.center=(500,400)
		screen.blit(msg,msgpos)
		pygame.time.delay(100)

	def win1():
		fontx = pygame.font.Font(f1, 30)
		msg=fontx.render(w1,True,black,yellow)
		msgpos=msg.get_rect()
		msgpos.center=(500,400)
		screen.blit(msg,msgpos)
		pygame.time.delay(100)

	def win2():
		fontx = pygame.font.Font(f1, 30)
		msg=fontx.render(w2,True,black,yellow)
		msgpos=msg.get_rect()
		msgpos.center=(500,400)
		screen.blit(msg,msgpos)
		pygame.time.delay(100)




	textRect.center = (startxp-40,startyp+25)
	textRect2.center=(endxp-40,endyp+20)
	screen.blit(text,textRect)
	screen.blit(text2,textRect2)
	screen.blit(player,(x,y))
	screen.blit(po,porect)
	pygame.display.flip()

	#speed
	if p==0:
		speed=speed1
	else:
		speed=speed2


	#clock
	time_passed=clock.tick()
	time_passed_seconds=time_passed/1000.0
	distance=time_passed_seconds*speed
	if bl1==1 and br1==0:
		bs1+=distance
		if bs1>900:
			bl1=0
			br1=1
	if bl2==1 and br2==0:
		bs2+=distance
		if bs2>900:
			bl2=0
			br2=1
	if bl3==1 and br3==0:
		bs3+=distance
		if bs3>900:
			bl3=0
			br3=1
	if bl4==1 and br4==0:
		bs4+=distance
		if bs4>900:
			bl4=0
			br4=1
	if bl5==1 and br5==0:
		bs5+=distance
		if bs5>900:
			bl5=0
			br5=1

	if bl1==0 and br1==1:
		bs1-=distance
		if bs1<0:
			bl1=1
			br1=0	
	if bl2==0 and br2==1:
		bs2-=distance
		if bs2<0:
			bl2=1
			br2=0	
	if bl3==0 and br3==1:
		bs3-=distance
		if bs3<0:
			bl3=1
			br3=0
	if bl4==0 and br4==1:
		bs4-=distance
		if bs4<0:
			bl4=1
			br4=0	
	if bl5==0 and br5==1:
		bs5-=distance
		if bs5<0:
			bl5=1
			br5=0
	#keys
	keys=pygame.key.get_pressed()

	if keys[pygame.K_LEFT] and x>=val:
		x=x-val
	if keys[pygame.K_RIGHT] and x<screenwidth-width-val:
		x=x+val
	if keys[pygame.K_UP] and y >= val-10: 
		y=y-val
	if keys[pygame.K_DOWN] and y < screenheight-height-val:
		y=y+val


	#points
	#fix
	if p==0:
		if y<490:
			pl[0]=1
		if y<360:
			pl[1]=1
		if y<260:
			pl[2]=1
			pl[3]=1
		if y<160:
			pl[4]=1
		if y<60:
			pl[5]=1
			pl[6]=1
			pl[7]=1
		if y<50:
			pl[8]=1
			pl[9]=1
		if y<430:
			pl[10]=1
		if y<330:
			pl[11]=1
		if y<230:
			pl[12]=1
		if y<130:
			pl[13]=1
		if y<30:
			pl[14]=1


	if p==1:
		if y>30:
			pl[8]=1
			pl[9]=1
		if y>130:
			pl[5]=1
			pl[6]=1
			pl[7]=1
		if y>230:
			pl[4]=1
		if y>330:
			pl[3]=1
			pl[2]=1
		if y>430:
			pl[1]=1
		if y>470:
			pl[0]=1
		if y>460:
			pl[10]=1
		if y>380:
			pl[11]=1
		if y>280:
			pl[12]=1
		if y>180:
			pl[13]=1
		if y>80:
			pl[14]=1

	if x>=120 and x<=190  and  y>=460 and y<=545: #1
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
		#pygame.time.delay(1000)
	if x>=570 and x<=640  and  y>=360 and y<=440: #2
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=10 and x<=70  and  y>=260 and y<=340: #3
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=770 and x<=840  and  y>=260 and y<=340: #4
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=370 and x<=440  and  y>=160 and y<=240: #5
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=0 and x<=70  and  y>=60 and y<=140: #6
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=170 and x<=240  and  y>=60 and y<=140: #7
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=590 and x<=660  and  y>=60 and y<=140: #8
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=320 and x<=390  and  y>=-40 and y<=40: #9
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=770 and x<=840  and  y>=-40 and y<=40: #10
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()

	if x>=bs1-30 and x<=bs1+40  and  y>=10 and y<=80: #b1
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=bs2-30 and x<=bs2+40  and  y>=110 and y<=180: #b2
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=bs3-30 and x<=bs3+40  and  y>=210 and y<=280: #b3
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=bs4-30 and x<=bs4+40  and  y>=310 and y<=380: #b4
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if x>=bs5-30 and x<=bs5+40  and  y>=410 and y<=480: #b5
		if(p==0):
			p=1
			player=player2
			x=endxp
			y=endyp
		else:
			p=0
			player=player1
			x=startxp
			y=startyp
		t=s
		s=e
		e=t
		t0=t1
		if ct==0:
			ct=1
			pt1=dts
			s1=pn
		elif ct==1:
			ct=2
			pt2=dts
			s2=pn
		pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
		#f.write("hit an obstacle\n")
		fail()
		#pygame.time.delay(500)
	if p==0: 
		if x>=460 and x<=530 and y>=-20 and y<=10:
			p=1
			t0=t1
			player=player2
			x=endxp
			y=endyp
			t=s
			s=e
			e=t
			if ct==0:
				ct=1
				pt1=dts
				s1=pn
			elif ct==1:
				ct=2
				pt2=dts
				s2=pn
			pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
			#f.write("Success\n")
			succ()

	if p==1:
		if x>=460 and x<=530 and y>=480 and y<=530:
			p=0
			t0=t1
			player=player1
			x=startxp
			y=startyp
			t=s
			s=e
			e=t
			if ct==0:
				ct=1
				pt1=dts
				s1=pn
			elif ct==1:
				ct=2
				pt2=dts
				s2=pn
			pl[0]=pl[1]=pl[2]=pl[3]=pl[4]=pl[5]=pl[6]=pl[7]=pl[8]=pl[9]=pl[10]=pl[11]=pl[12]=pl[13]=pl[14]=0
			#f.write("Success\n")
			succ()
	if ct==2:
		#print(pt1,pt2)
		#print(s1,s2)
		if s1>s2:
			#print("player1 is winner")
			#f.write("player1 is winner\n")
			win1()
			speed1=speed1+10
		elif s1<s2:
			#print("player2 is winner")
			#f.write("player2 is winner\n")
			speed2=speed2+10
			win2()
		else:
			if pt1>pt2:
				#print("player2 is winner")
				#f.write("player2 is winner\n")
				speed2=speed2+10
				win2()
			else:
				#print("player1 is winner")
				#f.write("player1 is winner\n")
				speed1=speed1+10
				win1()
		ct=0
		s1=0
		s2=0
		pt1=0
		pt2=0

	pygame.display.update()
	clock.tick(speed)
	#f.close()