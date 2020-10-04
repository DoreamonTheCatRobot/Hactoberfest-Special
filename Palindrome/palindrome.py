def oneDigit(num): 
	return ((num >= 0) and
			(num < 10)); 
      
def isPalUtil(num, dupNum): 
	if (oneDigit(num)): 
		return (num == (dupNum) % 10); 
    
	if (isPalUtil(int(num / 10), dupNum) == False): 
		return -1; 

	dupNum = int(dupNum / 10); 
	return (num % 10 == (dupNum) % 10); 
  
def isPal(num): 
	if (num < 0): 
		num = (-num); 
	dupNum = (num); # *dupNum = num 
	return isPalUtil(num, dupNum); 
  
n = 12321; 
if(isPal(n) == 0): 
	print("Yes"); 
else: 
	print("No"); 

n = 12; 
if(isPal(n) == 0): 
	print("Yes"); 
else: 
	print("No"); 

n = 88; 
if(isPal(n) == 1): 
	print("Yes"); 
else: 
	print("No"); 

n = 8999; 
if(isPal(n) == 0): 
	print("Yes"); 
else: 
	print("No");
