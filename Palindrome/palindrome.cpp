#include <stdio.h> 
int oneDigit(int num) 
{ 
	return (num >= 0 && num < 10); 
} 
bool isPalUtil(int num, int* dupNum) 
{ 
	if (oneDigit(num)) 
		return (num == (*dupNum) % 10); 
	if (!isPalUtil(num/10, dupNum)) 
		return false; 
	*dupNum /= 10; 
	return (num % 10 == (*dupNum) % 10); 
} 

int isPal(int num) 
{ 
	if (num < 0) 
	num = -num; 

	int *dupNum = new int(num);

	return isPalUtil(num, dupNum); 
} 
int main() 
{ 
	int n = 12321; 
	isPal(n)? printf("Yes"): printf("No"); 

	n = 12; 
	isPal(n)? printf("Yes"): printf("No"); 

	n = 88; 
	isPal(n)? printf("Yes"): printf("No"); 

	n = 8999; 
	isPal(n)? printf("Yes"): printf("No"); 
	return 0; 
} 
