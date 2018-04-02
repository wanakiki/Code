## 93. Restore IP Addresses
##### 2018-04-02 21:19:30
##### dfs
***
## 1.题目
>Given a string containing only digits, restore it by returning all possible valid IP address combinations.
>
>For example:
Given "25525511135",
>
>return ["255.255.11.135", "255.255.111.35"]. (Order does not matter)
>
>给定一个只包含数字的字符串，通过返回所有可能的有效IP地址组合来恢复它。返回顺序不做要求。

## 2.分析
一道回溯题，还是不能够独立的想出来自己的解决方式。还需要多加练习。回溯一定要注意层次性。

有关于ip：由四段组成，每段取值可为0~255，段与段之间用'.'隔开，每段数字不允许出现前导零。
因为ip的特点，我们可以用多种方式来提前终止回溯。遍历到的0必须占一位。（代码中与零相关的解决方式的确没想到）
## 3.代码
```cpp
class Solution{
public:
  vector<string> restoreIpAddresses(string s){
    vector<string> res;
    string ip;
    dfs(s,0,0,ip,res);
    return res;
  }
  void dfs(string s,int start,int step,string ip,vector<string> &res){
    if(start==s.size() && step==4){
      ip.erase(ip.end()-1);   //去掉最后的点
      res.push_back(ip);  
      return ;
    }
    if(s.size()-start > (4-step)*3) return;   //过长终止搜索
    if(s.size()-start < (4-step) )  return;   //长度不足终止
    int num=0;
    for(int i=start;i<start+3;i++){   //开始深度搜索
      num=num*10+s[i]-'0';
      if(num<=255){
        ip+=s[i];
        dfs(s,i+1,step+1,ip+'.',res);
      }
      if(num==0) break;   //零只能出现一次
    }
  }
};
```
这是C++最快的方法，分三种情况考虑每段的字符数
```cpp
class Solution {
public:
    vector<string> restoreIpAddresses(string s) {
        helper(s, 0, 0);
        return ans;
    }
private:
    vector<string> ans;
    string ele;
    void helper(string s, int pos, int part){
        if (pos == s.size() && part == 4){ans.push_back(ele);}
        if (part >= 4){return;}
        if (!ele.empty()){ele.push_back('.');}
        // case one: 1 digit
        ele.push_back(s[pos]);
        helper(s, pos+1, part+1);
        ele.pop_back();
        // case two: 2 digits
        if (pos+1 < s.size() && s[pos] != '0'){
            ele += s.substr(pos, 2);
            helper(s, pos+2, part+1);
            ele.erase(ele.size()-2);
        }
        // case three: 3 digits
        if (pos+2 < s.size() && s[pos] != '0' && stoi(s.substr(pos,3)) <= 255){
            ele += s.substr(pos, 3);
            helper(s, pos+3, part+1);
            ele.erase(ele.size() - 3);
        }
        if (!ele.empty()){ele.pop_back();}
    }
};
```
