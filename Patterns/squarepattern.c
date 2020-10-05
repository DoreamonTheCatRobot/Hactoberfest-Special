/*
1  2  3  4   5   6  7  8  9  10
36 37 38 39  40  41 42 43 44 11
35 64 65 66  67  68 69 70 45 12
34 63 84 85  86  87 88 71 46 13
33 62 83 96  97  98 89 72 47 14
32 61 82 95  100 99 90 73 48 15
31 60 81 94  93  92 91 74 49 16
30 59 80 79  78  77 76 75 50 17
29 58 57 56  55  54 53 52 51 18
28 27 26 25  24  23 22 21 20 19

*/

#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
#include<dos.h>
int a[10][10],l,i=0,j,k=1,n=10;  // Two Dimensional Array
int square()
{

    for(l=0;l<n-2;l++)   // For Number of Squares Required
    {
      i=l;

    for(j=l;j<n-l;j++)  // For First Edge of the Square
    {
        a[i][j]=k;
        if(k>(n*n))
            return 0;
        k++;

    }
    for(i=i+1,j=j-1;i<n-l;i++)  // For Second Edge of the Square
    {

        a[i][j]=k;
           if(k>(n*n))
            return 0;
        k++;

    }
    for(j=j-1,i=i-1;j>=l;j--)  // For Third Edge of the Square
    {
        a[i][j]=k;
           if(k>(n*n))
            return 0;
        k++;

    }
    for(i=i-1,j=j+1;i>=l+1;i--)  // For Fourth Edge of the Square
    {
        a[i][j]=k;
           if(k>(n*n))
            return 0;
        k++;
    }
    }
}
void main()
{
    int x,y;
    square();
    for(x=0;x<n;x++)
    {
    for(y=0;y<n;y++)
    {
    printf("%4d",a[x][y]);  // Two dimensional array
    }
        printf("\n");
    }
}


