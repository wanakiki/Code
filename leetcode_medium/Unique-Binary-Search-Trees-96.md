## 96. Unique Binary Search Trees
##### 2018-04-16 23:36:25
##### 中序二叉树
***
## 1. 题目
>Given n, how many structurally unique BST's (binary search trees) that store values 1...n?  
给定n，存储值1 ... n的结构唯一BST（二叉搜索树）有多少？

>For example,
Given n = 3, there are a total of 5 unique BST's.  
例如，给定n = 3，总共有5个独特的BST。
```
1         3     3      2      1
   \       /     /      / \      \
    3     2     1      1   3      2
   /     /       \                 \
  2     1         2                 3
```
## 2.分析
给定一个数字n，返回可以构成的二叉搜索树的总数。  
因为二叉搜索树的排列情况在不考虑重复的情况下只与个数有关，并且总数等于左支乘以右支，所以递归的思路很容易就想出来了，但是测试发现超时，参考网上的代码，改换了动态规划，成功提交。
## 3.代码
递归
```cpp
class Solution {
public:
    int numTrees(int n) {
        if(n<=1)
            return 1;
        int num=0;
        for(int i=1;i<n+1;i++){
            num+=numTrees(i-1)*numTrees(n-i);
        }
        return num;
    }
};
```
动态规划
```cpp
class Solution {
public:
    int numTrees(int n){
        /*int *res;
        res=new int[n+1];*/
        //本来打算用整形数组，但是因为没有赋初始值出现错误，直接采用了vecotr
        vector <int> res(n+1,0);
        res[0]=1;
        res[1]=1;
        for(int i=2;i<=n;i++)
            for(int j=0;j<i;j++)
                res[i]+=res[j]*res[i-j-1];
        return res[n];
    }
};
```

### 卡塔兰数
>dp[2] =  dp[0] * dp[1]　　　(1为根的情况)
>
>　　　+ dp[1] * dp[0]　　  (2为根的情况)
>
>同理可写出 n = 3 的计算方法：
>dp[3] =  dp[0] * dp[2]　　　(1为根的情况)
>
>　　　　+ dp[1] * dp[1]　　  (2为根的情况)
>
> 　　　  + dp[2] * dp[0]　　  (3为根的情况)
