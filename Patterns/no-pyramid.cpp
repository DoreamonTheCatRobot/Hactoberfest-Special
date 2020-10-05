/*
1
2  6
3  7  10
4  8  11  13
5  9  12  14  15
*/

#include <iostream>
using namespace std;
int main(){
    int n,i,c,a,m;
    cout<<"enter rows: ";
    cin>>n;
    for(int i=1;i<=n;i++){
        a=0;
        c=n-1;
        m=i;
        for(int j=1;j<=i;j++){
            cout<<m+a<<"\t";
        m=m+a;
        a=c;
        c--;
    }
        cout<<endl;
    }
}
