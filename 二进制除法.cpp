#include<bits/stdc++.h>
using namespace std;
int main(){
  string s;
  cin>>s;
  int sum = 0;
  for(int i=s.size()-1;i>0;i--){
    if(s[i]=='0'){
      sum++;
      continue;
    }
    else{
      sum+=2;
      for(i--;i>0;i--){
        if(s[i]=='1'){
          sum++;
        }
        else{
          s[i]='1';
          i++;
          break;
        }
      }
    }
  }
  cout<<sum;
}
