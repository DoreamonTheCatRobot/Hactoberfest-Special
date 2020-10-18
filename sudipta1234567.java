
//Write a program to display the least no from n after deleting k digit. If the input number is 36945 and k=3 the least number is 34 after deleting 3 digit
//sudipta kumar sahoo


import java.util.*;
class Q15
{
public static void main(String args[])
{
	int count=0,newn=0;
	Scanner ob=new Scanner(System.in);
	System.out.println("Enter the number:");
	int num=ob.nextInt();
	int n=num;
	int arr[]=new int[100];
	for(int i=0;i<n;i++)
	{
	while(n!=0)
	{
	int d=n%10;
	arr[i]=d;
	i++;
	count++;
	n/=10;
	}}
	for(int i=0;i<count;i++)
	System.out.print(arr[i]);
	System.out.println("\n"+count);

	for (int i = 0; i < count-1; i++)

	{

		

	for (int j = 0; j < count-i-1; j++)
  
	{
	
		if (arr[j] > arr[j+1])
 
		{
	
		int temp;

		temp=arr[j];

		arr[j]=arr[j+1];

		arr[j+1]=temp;

		}

	}

	}

	

	System.out.println("\n"+count);
	for(int i=0;i<count;i++)
	System.out.print(arr[i]);

	System.out.print("Enter the value of k:");
	int k=ob.nextInt();

	for(int i=0;i<count-k;i++)
	{
	newn=newn*10+arr[i];
	}
	System.out.println(newn);	
}}