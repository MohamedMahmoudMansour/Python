import time
import os

n = 5

while(1):
	k = 0

	time.sleep(0.5)
	# Upper Arrow
	for i in range(1, n):
		for space in range(1, (n*3-i)+1):
			print(end="  ")

		while k!=(2*i-1):
			print("* ", end="")
			k += 1

		k = 0
		print()
		
	for i in range(0, n):
	 
		for j in range(0, n*5):
			print(end=" ")
	 
		for j in range(0, n*5):
			if j == i:
				print("   *", end=" ")
					
		print()
	print()

	time.sleep(0.5)
	#Right Arrow
	o = n-1
	for i in range (o):
		if i== o-1:
			print ((o)* "       ",end = "        ")
			print ((2)* "* * * * * *  ")
		else :
			print ((2*o)* "      ",end = "      ")
			print ((i+1)* "* ")
	for j in range (o-1,0,-1):
		print ((2*o)* "      ",end = "      ")
		print (j* "* ")	

	time.sleep(0.5)
	# Down Arrow
	for i in range(0, n):
	 
		for j in range(0, n*5):
			print(end=" ")
	 
		for j in range(0, n*5):
			if j == i:
				print("   *", end=" ")
					
		print()

	for i in range(n, 1, -1):
		for space in range(0, (n*3-i+1)):
			print("  ", end="")
		for j in range(i, 2*i-1):
			print("* ", end="")
		for j in range(1, i-1):
			print("* ", end="")
		print()
		# Left Arrow
	# o = n-1
	# for i in range (o):
		# if i== o-1:
			# print ((o)* "       ",end = "        ")
			# print ((2)* "      * * * * * * * * * *")
		# else :
			# print ((2*o)* "      ",end = "      ")
			# print ((i+1)* "* ")
	# for j in range (o-1,0,-1):
		# print ((2*o)* "      ",end = "      ")
		# print (j* "* ")	

	
		
	time.sleep(0.5)
	os.system('cls')
	time.sleep(0.5)
	






