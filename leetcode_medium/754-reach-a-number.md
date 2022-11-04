## 754. 到达终点数字

2022-11-04 19:10:24

### 题目

在一根无限长的数轴上，你站在``0``的位置。终点在``target``的位置。

你可以做一些数量的移动 ``numMoves`` :


- 每次你可以选择向左或向右移动。
- 第 ``i`` 次移动（从  ``i == 1`` 开始，到 ``i == numMoves`` ），在选择的方向上走 ``i`` 步。


给定整数 ``target`` ，返回到达目标所需的 **最小**移动次数(即最小 ``numMoves`` )。

 

**示例 1:**

```
输入: target = 2
输出: 3
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 -1 。
第三次移动，从 -1 到 2 。
```

**示例 2:**

```
输入: target = 3
输出: 2
解释:
第一次移动，从 0 到 1 。
第二次移动，从 1 到 3 。
```

 

**提示:**


- ``-10<sup>9</sup> <= target <= 10<sup>9</sup>``
- ``target != 0``



[LeetCode链接](https://leetcode-cn.com/problems/reach-a-number/)

### 思路及代码

好题，做的数学相关题目比较少，连偶数的情况都没想到，直接开始暴搜结果超时，尝试直接使用二分查找又没有好的判别方式。

引用下评论区的解法：

> 简单题中的极品。 。。。 首先由于对称性，target是正是负影响不大。
> 
> 因为比如达到target=2=1-2+3.
> 
> 如果是-2，那就是-2=-1+2-3
> 
> 所以相当于是完全对称的一个选择。
> 
> 那么不妨设这个target是正的（用abs函数）
> 
> 所以我们尽量往右移动就可以达到目的地。
> 
> 假设1+2+3+...+k=sum
> 
> 如果sum=target，毫无疑问那么k就是最终答案。#1
> 
> 如果sum>target，而且sum-target是一个偶数，那么我们可以翻转一个数字的符号来完成等式。
> 
> 比如sum-target=4，那么我们把2变成-2，那么sum减小了4.
> 
> 这是由于（1+2+3+...k）-（1-2+3...k）=4
> 
> 也就是可以归结为：
> 
> 当sum-target为偶数，1+...-（sum-target）/2+...+k=target，那么答案依然是k。#2
> 
> 当sum-target为奇数，那么sum-target+1是一个偶数
> 
> 类似#2的证明，1+...-(sum-target+1)/2+...k=target-1
> 
> 此时再考虑k的奇偶性。
> 
> 如果k是偶数并且k>sum-target+1
> 
> 那么1+...-(sum-target+1)/2+....-(k/2)...+k+(k+1)=target
> 
> 由#2相似可证，相当于在1+2....+k+(k+1)减去了sum-target+1和k。
> 
> 等价于sum+（k+1）-sum+target-1-k====>target也就是答案是k+1.#3
> 
> 如果k=sum-target+1，由#3可知依然是k+1.#4
> 
> 如果k是奇数：
> 
> 1+2+...-(sum-target+1)/2.....+k-(k+1)+(k+2)=sum-(sum-target+1)+1=target,
> 
> 因此答案是k+2.#5
> https://leetcode.cn/u/_wang66/

```cpp
class Solution {
public:
    int reachNumber(int target) {
        target = abs(target);

        int res = 0;
        int cur_val = 0;
        while(cur_val < target){
            res++;
            cur_val += res;
        }

        int left = cur_val - target;
        if(left % 2 == 0)   return res;
        else{
            if(res % 2 == 0)   return res + 1;
            else                return res + 2;
        }
    }
};
```