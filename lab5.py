import random
x=0
while (x<=100):
	n=input("enter q to quit and enter r to roll the dice:")

	if(n=='q'):
		print("bye")
		exit()
	elif(n=='r'):
		r=random.randint(1,6)
		print("your score is ",r) 
		x=x+r
		if(x<=100):
				if(x==100):
					print("you won")
				elif(x==8):
					x=37
					print("you got a ladder,your score is",x)
				elif(x==11):
					x==2
					print("you've been eaten by a snake",x)
				elif(x==13):
					x==34
					print("you got a ladder,your score is",x)
				elif(x==25):
					x==4	
					print("you've been eaten by a snake",x)	
				elif(x==38):	
					x==9	
					print("you've been eaten by a snake",x)
				elif(x==40):
					x==68
					print("you got a ladder,your score is",x)
				elif(x==52):
					x==81
					print("you got a ladder,your score is",x)
				elif(x==65):
					x==46
					print("you've been eaten by a snake",x)
				elif(x==76):
					x==97
					print("you got a ladder,your score is",x)
				elif(x==89):
					x==70
					print("you've been eaten by a snake",x)
				elif(x==93):
					x==64
					print("you've been eaten by a snake",x)
		
dl319@soetcse:~/tanuja$ python3 lab5.py
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r
your score is  4
you got a ladder,your score is 37
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r
your score is  5
enter q to quit and enter r to roll the dice:r
your score is  1
enter q to quit and enter r to roll the dice:r
your score is  4
enter q to quit and enter r to roll the dice:rr
enter q to quit and enter r to roll the dice:r
your score is  6
enter q to quit and enter r to roll the dice:r
your score is  4
enter q to quit and enter r to roll the dice:r
your score is  4
enter q to quit and enter r to roll the dice:r
your score is  5
enter q to quit and enter r to roll the dice:r
your score is  5
enter q to quit and enter r to roll the dice:r
your score is  4
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r  
your score is  6
enter q to quit and enter r to roll the dice:rr
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r
your score is  4
enter q to quit and enter r to roll the dice:r 
your score is  2
you've been eaten by a snake 93
enter q to quit and enter r to roll the dice:r
your score is  2
enter q to quit and enter r to roll the dice:r
your score is  5
you won
enter q to quit and enter r to roll the dice:q
bye
	


		
