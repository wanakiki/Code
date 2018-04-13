## 60. Permutation Sequence
##### 2018-04-13 23:39:45
***
## 1.题目
>给定n和k，返回第K个n!的排列。n与k皆小于等于9
## 2.分析
题目已经不算是算法题了，反倒是像一个找规律的题目，找到规律很容易的就能实现。  
下面的是参考代码，对于标志数组没有做弹出处理，而是将位置改变，节省了空间。

## 3，代码
```cpp
string getPermutation(int n, int k) {
    int i,j,f=1;  //标志数组分为左右两边 右边为已经用过的值
    string s(n,'0');
    for(i=1;i<=n;i++){
        f*=i;
        s[i-1]+=i;  //构造标志数组 采用string格式
    }
    for(i=0,k--;i<n;i++){
        f/=n-i;
        j=i+k/f; // 计算应该添加的值的地址
        char c=s[j];
        for(;j>i;j--)
            s[j]=s[j-1];  //将使用过的数据移动到右侧
        k%=f;
        s[i]=c;
    }
    return s;
};
```
