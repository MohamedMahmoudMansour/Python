import os 

print("\t\t\t\"Welcome to our Calculator\"")

print("\t(\"Programmer Mode press : (p)   and   Standard   Mode press : (s)\")")
print("                   (-------->( Exit  press  (e) )<--------)         ")
print("                   (-------->( Clear press  (c) )<--------)         ")


while (1):
	mode = input("Choose your mode : ")

	if mode == 'p':
		print("\t\t  #-----------> Programmer Mode <------------#\n")	
		while (1):
				print("01. Arithmetic Operators ( + , - , * , / ) press (a) \n02. Logical    Operators ( & , | , ^ , ~ ) press (g)")
				print("03. Conversions       (Bin, Dec, Oct, Hex) press (m) \n")
				prog_mode = input("press (a/g/m) and (b) for back : ")
				print()
				if prog_mode == 'a':
					while(1):
						Num_1   = int(input("Number 1 : "))
						operand = input("Operand : ")
						Num_2   = int(input("Number 2 : "))	
						
						if(operand == '+'):
							print(bin(Num_1)," + ",bin(Num_2)," = ",bin(Num_1+Num_2))
						elif (operand == '-'):	
							print(bin(Num_1)," - ",bin(Num_2)," = ",bin(Num_1-Num_2))
						elif (operand == '*'):	
							print(bin(Num_1)," * ",bin(Num_2)," = ",bin(Num_1*Num_2))
						elif (operand == '/'):	
							if Num_2 == 0:
								print("Can't make division of Zero")
							else:
								print(bin(Num_1)," / ",bin(Num_2)," = ",bin(int(Num_1/Num_2)))
						elif (operand == '%'):	
							print(bin(Num_1)," % ",bin(Num_2)," = ",bin(Num_1%Num_2))
						else:
							print("Wrong Operation")
						
						
						b = input("You want to conitnue (y/n): ")
						print("\t\t\t#================================#")
						if b == 'n':
							break		
							
				elif prog_mode == 'g':
					while(1):
						Num_1   = int(input("Number 1 : "))
						operand = input("Operand : ")
						Num_2   = int(input("Number 2 : "))	
						
						if(operand == '&'):
							print(bin(Num_1)," & ",bin(Num_2)," = ",bin(Num_1&Num_2))
						elif (operand == '|'):	
							print(bin(Num_1)," | ",bin(Num_2)," = ",bin(Num_1|Num_2))
						elif (operand == '^'):	
							print(bin(Num_1)," ^ ",bin(Num_2)," = ",bin(Num_1^Num_2))
						elif (operand == '>>'):	
							print(bin(Num_1)," >> ",bin(Num_2)," = ",bin(Num_1^Num_2))
						elif (operand == '<<'):	
							print(bin(Num_1)," << ",bin(Num_2)," = ",bin(Num_1^Num_2))
						elif (operand == '~'):	
							print(" ~ ",bin(Num_1)," = ",bin(~Num_1)," \n ~",bin(Num_2)," = ",bin(~Num_2))

						else:
							print("Wrong Operation")
						
						
						b = input("You want to conitnue (y/n): ")
						print("\t\t\t#================================#")
						if b == 'n':	
							break
							
				elif prog_mode == 'm':
					while (1):
						conv_type = input("Conversion Type :")
						print()
						if conv_type == 'D to B':
							print("Decimal to Binary")
							Num   = int(input("Number : "))
							print(Num," = ",bin(Num))
							
						elif conv_type == 'D to O':
							print("Decimal to Octal")
							Num   = int(input("Number : "))
							print(Num," = ",oct(Num))
							
						elif conv_type == 'D to H':
							print("Decimal to Hexadecimal")
							Num   = int(input("Number : "))
							print(Num," = ",hex(Num))
							
						elif conv_type == 'B to D':
							print("Binary to Decimal")
							Num   = int(input("Number : "),2)
							print(bin(Num)," = ",Num)
							
						elif conv_type == 'B to O':
							print("Binary to Octal")
							Num   = int(input("Number : "),2)
							print(bin(Num)," = ",oct(Num))				

						elif conv_type == 'B to H':
							print("Binary to Hexadecimal")
							Num   = int(input("Number : "),2)
							print(bin(Num)," = ",hex(Num))							

						elif conv_type == 'O to D':
							print("Octal to Decimal")
							Num   = int(input("Number : "),8)
							print(oct(Num)," = ",Num)
							
						elif conv_type == 'O to B':
							print("Octal to Binary")
							Num   = int(input("Number : "),8)
							print(oct(Num)," = ",bin(Num))
							
						elif conv_type == 'O to H':
							print("Octal to Hexadecimal")
							Num   = int(input("Number : "),8)
							print(oct(Num)," = ",hex(Num))
							
						elif conv_type == 'H to D':
							print("Hexadecimal to Decimal")
							Num   = int(input("Number : "),16)
							print(hex(Num)," = ",Num)
							
						elif conv_type == 'H to B':
							print("Hexadecimal to Binary")
							Num   = int(input("Number : "),16)
							print(hex(Num)," = ",bin(Num))
							
						elif conv_type == 'H to O':
							print("Hexadecimal to Octal")
							Num   = int(input("Number : "),16)
							print(hex(Num)," = ",oct(Num))
						else:
							print("Wrong Conversion!!!");
							
						b = input("You want to conitnue (y/n): ")
						print("\t\t\t#================================#")
						if b == 'n':
							break
							
				elif prog_mode == 'b':
					break

	
	
	elif mode == 's':
		print("\t\t  #-----------> Standard Mode <------------#")
		while (1):
				Num_1   = int(input("Number 1 : "))
				operand = input("Operand : ")
				Num_2   = int(input("Number 2 : "))	
				
				if(operand == '+'):
					print(f"{Num_1} + {Num_2} = {Num_1+Num_2}")
				elif (operand == '-'):	
					print(f"{Num_1} - {Num_2} = {Num_1-Num_2}")
				elif (operand == '*'):	
					print(f"{Num_1} * {Num_2} = {Num_1*Num_2}")
				elif (operand == '/'):	
					if Num_2 == 0:
						print("Can't make division of Zero")
					else:
						print(f"{Num_1} / {Num_2} = {Num_1/Num_2}")
				elif (operand == '%'):	
					print(f"{Num_1} % {Num_2} = {Num_1%Num_2}")
				else:
					print("Wrong Operation")
				
				
				b = input("You want to conitnue (y/n): ")
				print("\t\t\t#================================#")
				if b == 'n':
					break
				
	elif mode == 'e':
		print("Thanks for using the Calculator.	")
		break	
	elif mode == 'c':
		os.system('cls')
		print("\t\t\t\"Welcome to our Calculator\"")
		print("\t(\"Programmer Mode press : (p)   and   Standard   Mode press : (s)\")")
		print("                   (-------->( Exit  press  (e) )<--------)         ")
		print("                   (-------->( Clear press  (c) )<--------)         ")
	else:
		print("Wrong Mode!!!!")