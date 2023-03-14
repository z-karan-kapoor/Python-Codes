#include<bits/stdc++.h>
using namespace std;

int Test2(string s){        //For single digit check
    int sum=0;
    for(int i=0;i<s.size();i++)
    {
        if(s[i]>='0' && s[i]<='9')
        {
            char ch=s[i];
            int x=int(ch) - 48 ;
            sum+=x;
        }
    }
    return sum;
}

int Test1(string s)         // For multiple digit check
{
    int sum=0,dig=0;
    for(int i=0;i<s.size();i++)
    {
        while(s[i]>='0' && s[i]<='9')
        {
            char ch=s[i];
            int x=int(ch) - 48 ;
            dig=(dig*10) + x;
            i++;
        }
        sum+=dig;
        dig=0;
    }
    return sum;
}

int main()
{
    string s;
    cout<<"Enter string: "<<endl;
    cin>>s;
    bool singleDig=0;
    cout<<"press 1 to check single digit else 0: "<<endl;
    cin>>singleDig;
    int ans=0;
    if(singleDig)
        ans=Test2(s);
    else
        ans=Test1(s);
    cout<<ans<<endl;
    return 0;
}