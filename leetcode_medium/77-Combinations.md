## 77. Combinations
##### 2018-04-06 12:48:33
##### dfs
***
## 1.题目
>Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.   
给定两个整数n和k，返回1 ... n中所有可能的k个数的组合。

If n = 4 and k = 2, a solution is:
```
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```
## 2.分析
题目比较明确，开始想到的是递归算法，写到一半之后发现不能对数据进行删除。  
因为对c++还不够了解，看了别人的解法之后才意识到还有pop_back可以使用。于是用dfs解决了题目，时间150ms......

## 3.
```cpp
class Solution {
public:
    vector<vector<int>> combine(int n, int k) {
        vector<vector<int>> res;
        if(n<k) return res;
        vector<int> temp(0);
        creat(res,temp,0,0,n,k);
        return res;
    }
    void creat(vector<vector<int>> &res,vector<int> temp,int start,int num,int n,int k){
      if(num==k){
          res.push_back(temp);
          return;
      }
      for(int i=start;i<n;i++){
        temp.push_back(i+1);
        creat(res,temp,i+1,num+1,n,k);
        temp.pop_back();
      }
    }
};
```
