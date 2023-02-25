## 386. 字典序排数

2022-04-18 17:29:04

### 题目

给你一个整数 ``n`` ，按字典序返回范围 ``[1, n]`` 内所有整数。

你必须设计一个时间复杂度为 ``O(n)`` 且使用 ``O(1)`` 额外空间的算法。



**示例 1：**

```

输入：n = 13
输出：[1,10,11,12,13,2,3,4,5,6,7,8,9]
```

**示例 2：**

```

输入：n = 2
输出：[1,2]
```



**提示：**


- ``1 <= n <= 5 * 10<sup>4</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/lexicographical-numbers/)

### 思路及代码

采用递归方法能够比较简单的写出来代码，由于题目数据范围限制在100000，递归深度优先，整体运行时间还可以接受。官方题解给出的是迭代实现，后面可能会补充一下。

```cpp
class Solution {
public:
vector<int> res;
void helper(int n, int cur){
    while(cur <= n ){
        res.push_back(cur);
        helper(n, cur * 10);
        if (cur % 10 == 9)
            break;
        cur++;   
    }
    return ;
}
    vector<int> lexicalOrder(int n) {
        helper(n, 1);
        return res;
    }
};
```