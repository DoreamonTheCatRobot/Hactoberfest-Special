/*
1
121
12321
1234321
123454321
12345654321
1234567654321 
*/

#include<iostream>
using namespace std;
int main()
{
    int n,m,a=0,b=1,k;
    cin>>n;
    for(int i=1;i<=n;i++)
    {
        for(int j=1;j<=i+a;j++)
        {
            if(j<i || j==i)
            {
                cout<<j;
            }
            else
            {
               m=i;
               k=m-b;
               cout<<k;
               b++;
            }
        }
        b=1;
        a++;
        cout<<endl;
    }
}
