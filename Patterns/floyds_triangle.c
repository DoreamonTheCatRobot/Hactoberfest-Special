/*
1
23
456
78910
*/
#include<stdio.h>
int main()
{
	int i,j,n,m=1;
	printf("enter the number: ");
	scanf("%d",&n);
	for(i=1;i<=n;i++)
	{
		for(j=1;j<=i;j++)
		{
			printf("%d",m);
			m++;
		}
		printf("\n");
	}
}
