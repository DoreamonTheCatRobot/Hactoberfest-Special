while True:
	try:
# Taking The Input From The User
		nC = int(input("Enter The Number Which You Want To Check\n"))  
		
		# Checks If nC Is A Prime Number  
		if nC > 1:  
		   for i in range(2,nC):  
		       if (nC % i) == 0:  
		           print("%s is not a prime number"%nC)  
		           break  
		   else:  
		       print(nC,"is a prime number")           
		else:  
		   print(nC,"is not a prime number")  
		break
	except ValueError:
		print("Enter a Integer only.")
