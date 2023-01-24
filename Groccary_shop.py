import sys
import time
import colorama
from colorama import Fore
colorama.init()


print ('\033[31m')

#Welcome page 
def delay_print(s):
    for c in s:
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.05)
		
delay_print("\n\t\t\t( Welcome to our GROCCARY Shop )\n")
print ('\033[39m')

#intialized data for Customer
cost = 0.0
product_count = 0



goods_counts = {
  "Apple " : 50,
  "Banana": 50,
  "Orange": 50,
  "Mango " : 50
}

goods_prices = {
  "Apple " : 26.95,
  "Banana": 19.95,
  "Orange": 19.95 ,
  "Mango " : 24.95
}

print("\nAdmin    Page press : (1)")
print("Customer Page press : (2)\n")


while 1:
	mode = input("Choose page : ")
	if mode == '1':
		print("\t\t=====================")
		print("\t\t   ( Admin Page ) \n")


	elif mode == '2':

		print("\t\t=====================")
		print("\t\t  ( Customer Page ) \n")
		print("01.  Show our products press (1)")
		print("02.  Start shopping    press (2)")
		print("03.  Back to home Page press (3)")

		while 1:
			mode = input("Choice : ")

			if mode == '1':
				print("\nPrices:-")
				for items,values in goods_prices.items():
					print(items,"=",values,"EGP/KG")
					
				print("\nAmounts:-")
				for items,values in goods_counts.items():
					print(items,"=",values,"KG")
					
				print()
					
			elif mode == '2':			
				print("\nChoose Product and Amount :-\n")
				
				while 1:
					product = input("Product or Total Cost : ")
					
					if product == "Apple":
						amount  = int(input("Amount : "))
						if(amount > goods_counts["Apple "]):
							print("\t\t    Sorry, We can't provide this quantity")
							print("\t\tPlease, choose low quantity or another product\n")
							# print("\t\t=====================")
							

						else:					
							cost =  cost + (goods_prices["Apple "] * amount)
							goods_counts["Apple "] = goods_counts["Apple "] - amount
							# print("\t\t=====================")
							print()
					
					elif product == "Banana":
						amount  = int(input("Amount : "))
						if(amount > goods_counts["Banana"]):
							print("\t\t    Sorry, We can't provide this quantity")
							print("\t\tPlease, choose low quantity or another product\n")
							# print("\t\t=====================")
						
						else:
							cost = cost +(goods_prices["Banana"] * amount)
							goods_counts["Banana"] = goods_counts["Banana"] - amount
							# print("\t\t=====================")
							print()
					
					elif product == "Orange":
						amount  = int(input("Amount : "))
						if(amount > goods_counts["Orange"]):
							print("\t\t    Sorry, We can't provide this quantity")
							print("\t\tPlease, choose low quantity or another product\n")
							# print("\t\t=====================")
						
						else:
							cost = cost + (goods_prices["Orange"] * amount)
							goods_counts["Orange"]  = goods_counts["Orange"] - amount
							# print("\t\t=====================")
							print()
							
					elif product == "Mango":
						amount  = int(input("Amount : "))
						if(amount > goods_counts["Mango "]):
							print("\t\t    Sorry, We can't provide this quantity")
							print("\t\tPlease, choose low quantity or another product\n")
							# print("\t\t=====================")
						
						else:
							cost = cost + (goods_prices["Mango "] * amount)
							goods_counts["Mango "]  = goods_counts["Mango "] - amount
							# print("\t\t=====================")
							print()
					elif product == "cost":
						print("Total cost =",cost, "EGP\n")
						cont = input("continue ? (y/n):")
						if cont == 'n':
							print("\n\t\t   ===============")
							break
							
							
					else :
						print("Sorry, This product does not exit")
						print("Please, choose another one")
						print("\n\t\t   ===============")
			elif mode == '3':
				print("\n\t\t=====================")
				break
