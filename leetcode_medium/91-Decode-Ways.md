## 91. Decode Ways
##### 2018-03-29 23:00:27
##### 动态规划
***
## 1.题目
>A message containing letters from A-Z is being encoded to numbers using the following mapping: 
>```
>'A' -> 1
>'B' -> 2
>...
>'Z' -> 26
>```
>Given an encoded message containing digits, determine the total number of ways to decode it.   
>将二十六个字母分别与数字相对应，给定一个由数字组成的字符串，写一个函数解出其能翻译成多少中英文字符。

for example,  
Given encoded message "12", it could be decoded as "AB" (1 2) or "L" (12).

The number of ways decoding "12" is 2. 
## 2.分析
开始用递归，发现不能实现之后查到这道题目还是动态规划。可能差评比较多的原因是因为题目简单但是讨论的情况很多。了解动态规划的方法，考虑所有情况，分开讨论就能实现。  
要注意，100无法解码，110只有一种解码。
详细的可以看下面这个图：
![tup](https://img-blog.csdn.net/20150618181426177)
来自[csdn博客](https://blog.csdn.net/u012501459/article/details/46550815)
## 3代码
```c
int numDecodings(char* s) {
  int len=strlen(s);
  if(len==0)
    return 0;
  int dp[len];
  for(int i=0;i<len;i++)
    dp[i]=0;
  dp[0]=(*s=='0')?0:1;
    
  for(int i=1;i<len;i++){
    if(s[i]=='0'){
      if(s[i-1]=='1' || s[i-1]=='2'){
        if(i>=2)
          dp[i]=dp[i-2];
        else
          dp[i]=dp[i-1];
      }
      else
        return 0; //针对100的情况
    }
    else if((s[i-1]=='1' || (s[i-1]=='2' &&s[i]<='6')))
      if(i>=2)
        dp[i]+=dp[i-2]+dp[i-1];
      else
        dp[i]=dp[i-1]+1;
    else
      dp[i]+=dp[i-1];
  }
  return dp[len-1];
}
```

2021年4月21日

今天错了几次之后终于过了，还是使用动态规划方法，可以通过补充两个无用字符来减少特殊情况的处理。需要注意的一点是，对于0这个特殊值，只能与前一个数字构成某种字母，动态规划时需要注意。

```cpp
class Solution {
public:
    int numDecodings(string s) {
        s = "  " + s;
        int len = s.size();
        vector<int> dp(len, 1);
        for(int i = 2; i < len; i++){
            if(s[i-1] == '1'){
                if(s[i] == '0') dp[i] = dp[i-2];
                else dp[i] = dp[i-1]  + dp[i-2];
            }
            else if(s[i-1] == '2' && s[i] < '7'){
                if(s[i] == '0') dp[i] = dp[i-2];
                else dp[i] = dp[i-1]  + dp[i-2];
            }
            else{
                if(s[i] == '0'){
                    return 0;
                }
                else{
                    dp[i] = dp[i-1];
                }
            }
        }
        return dp[len-1];
    }
};
```
