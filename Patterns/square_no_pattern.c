/*
555555555
544444445
543333345
543222345
543212345
543222345
543333345
544444445
555555555
*/


#include <stdio.h>
#include <string.h>
#include <math.h>
#include <stdlib.h>
int main()
{
    int n;
    scanf("%d",&n);
    if(n>=1 && n<=1000){
    int a[2*n-1][2*n-1],i=0,j=0,k=n,st=0,end=2*n-1;
    while(1)
    {
        i=st;
        j=st;
        for(j=st;j<end;j++)
        {
            a[i][j]=k;
            if(a[i][j]==1)
               break;
        }
        if(a[i][j]==1)
           break;
        
        j=end-1;
        for(i=st;i<end;i++)
        {
            a[i][j]=k;
            if(a[i][j]==1)
           break;
        }
        if(a[i][j]==1)
           break;
        i=end-1;
        for(j=end-1;j>=st;j--)
        {
            a[i][j]=k;
            if(a[i][j]==1)
           break;
        }
        if(a[i][j]==1)
           break;
        j=st;
        for(i=end-1;i>=st;i--)
        {
            a[i][j]=k;
            if(a[i][j]==1)
           break;
        }
        st++;
        end--;
        k--;
        if(a[i][j]==1)
           break;
    }
    // printing 
    for(i=0;i<2*n-1;i++)
    {
        for(j=0;j<2*n-1;j++)
            {
                printf("%d ",a[i][j]);
            }
            printf("\n");
    }
    }
    return 0;
}



