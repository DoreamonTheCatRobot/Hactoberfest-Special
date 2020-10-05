using System; 

class GFG 
{ 

public static int oneDigit(int num) 
{ 
	if((num >= 0) &&(num < 10)) 
	return 1; 
	else
	return 0; 
} 

public static int isPalUtil(int num, 
							int dupNum) 
{ 
	if (oneDigit(num) == 1) 
		if(num == (dupNum) % 10) 
		return 1; 
		else
		return 0; 

	if (isPalUtil((int)(num / 10), dupNum) == 0) 
		return -1; 
    
	dupNum = (int)(dupNum / 10); 
	if(num % 10 == (dupNum) % 10) 
		return 1; 
	else
		return 0; 
} 

public static int isPal(int num) 
{ 
	if (num < 0) 
	num = (-num); 
	int dupNum = (num);
	return isPalUtil(num, dupNum); 
} 

public static void Main() 
{ 
int n = 12321; 
if(isPal(n) == 0) 
	Console.WriteLine("Yes"); 
else
	Console.WriteLine("No"); 

n = 12; 
if(isPal(n) == 0) 
	Console.WriteLine("Yes"); 
else
	Console.WriteLine( "No"); 

n = 88; 
if(isPal(n) == 1) 
	Console.WriteLine("Yes"); 
else
	Console.WriteLine("No"); 

n = 8999; 
if(isPal(n) == 0) 
	Console.WriteLine("Yes"); 
else
	Console.WriteLine("No"); 
} 
}
