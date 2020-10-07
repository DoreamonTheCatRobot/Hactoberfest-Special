def half(n): 
	for i in range(0, n): 
		for j in range(0, i+1): 
			print("* ",end="") 
		print("\r") 
while True:
	try:
		n = int(input("Enter the number of rows in pyramid you want:"))
		half(n) 
		break
	except ValueError:
		print("Enter a Integer only.")
