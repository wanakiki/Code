## 942. 增减字符串匹配

2022-05-09 17:29:09

### 题目

由范围 ``[0,n]`` 内所有整数组成的 ``n + 1`` 个整数的排列序列可以表示为长度为 ``n`` 的字符串 ``s`` ，其中:


- 如果 ``perm[i] < perm[i + 1]`` ，那么 ``s[i] == 'I'``
- 如果 ``perm[i] > perm[i + 1]`` ，那么 ``s[i] == 'D'``


给定一个字符串 ``s`` ，重构排列 ``perm`` 并返回它。如果有多个有效排列perm，则返回其中 **任何一个** 。



**示例 1：**

```
输入：s = "IDID"
输出：[0,4,1,3,2]
```

**示例 2：**

```
输入：s = "III"
输出：[0,1,2,3]
```

**示例 3：**

```
输入：s = "DDI"
输出：[3,2,0,1]
```



**提示：**


- ``1 <= s.length <= 10<sup>5</sup>``
- s 只包含字符 ``"I"`` 或 ``"D"``



[LeetCode链接](https://leetcode-cn.com/problems/di-string-match/)

### 思路及代码

遍历字符串，统计其中字母 I 的个数 count，令 n - count 作为 perm 的第一个元素，采用双指针对记录递增和递减区间当前的元素，根据字符串的字母进行填充即可。

```cpp
class Solution {
public:
    vector<int> diStringMatch(string s) {
        int len = s.size();
        vector<int> res(len + 1, 0);
        int count = 0;
        for(int i = 0; i < len; i++){
            if(s[i] == 'I') count++;
        }

        res[0] = len - count;
        int i_num = res[0] + 1;
        int d_num = res[0] - 1;
        for(int i = 0; i < len; i++){
            if(s[i] == 'I'){
                res[i+1] = i_num++;
            }
            else{
                res[i+1] = d_num--;
            }
        }
        return res;
    }
};
```

虽然是简单题，个人思考起来却感觉有些困难，查看官方题解之后发现可以直接用贪心搭配双指针来做，假设当前字母是 I 则 perm 中对应位置可直接填充最小值，如果是 D 可直接填充最大值。

```cpp
class Solution {
public:
    vector<int> diStringMatch(string s) {
        int len = s.size();
        vector<int> res(len + 1, 0);
        int left = 0, right = len;
        for(int i = 0; i < s.size(); i++){
            if(s[i] == 'I'){
                res[i] = left++;
            }
            else{
                res[i] = right--;
            }
        }
        res[len] = left;
        return res;
    }
};
```
