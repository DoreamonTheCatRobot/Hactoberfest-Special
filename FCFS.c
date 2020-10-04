#include<stdio.h>
#include<conio.h>
#define max 30

void main()
{
	int i,j,n,bt[max],wt[max],tat[max] ;  //n=no.of process,bt= burst time array, wt=waiting time array,tat=turn around time array
	float awt=0,atat=0;      //awt=average waiting time,atat=average turn around time
	printf("Enter the total number of processes : ");
	scanf("%d",&n);
	printf("Enter the burst time for the processes :\n");
	for(i=0;i<n;i++)
	{
		scanf("%d",&bt[i]);
	}
	printf("Process\t Burst Time\t Waiting Time\t Turn Arround Time\n");
	for(i=0;i<n;i++)
	{
		wt[i]=0;
		tat[i]=0;
		for(j=0;j<i;j++)
		{
			wt[i]=wt[i]+bt[j];
		}
		tat[i]=wt[i]+bt[i];
		awt=awt+wt[i];
		atat=atat+tat[i];
		printf("%d\t%d\t\t%d\t\t%d\n",i+1,bt[i],wt[i],tat[i]);
	}
	awt=awt/n;
	atat=atat/n;
	printf("Average Waiting Time : %f\n",awt);
	printf("Average Turn Arround Time : %f",atat);
}
