## 1839. 解码异或后的数组

2021-05-06 10:43:02

### 题目

**未知** 整数数组 ``arr`` 由 ``n`` 个非负整数组成。

经编码后变为长度为 ``n - 1`` 的另一个整数数组 ``encoded`` ，其中 ``encoded[i] = arr[i] XOR arr[i + 1]`` 。例如，
``arr = [1,0,2,1]`` 经编码后得到 ``encoded = [1,2,3]`` 。

给你编码后的数组 ``encoded`` 和原数组 ``arr`` 的第一个元素 ``first``（``arr[0]``）。

请解码返回原数组 ``arr`` 。可以证明答案存在并且是唯一的。

 

**示例 1：**

```

输入：encoded = [1,2,3], first = 1
输出：[1,0,2,1]
解释：若 arr = [1,0,2,1] ，那么 first = 1 且 encoded = [1 XOR 0, 0 XOR 2, 2 XOR 1] = [1,2,3]
```

**示例 2：**

```

输入：encoded = [6,2,7,3], first = 4
输出：[4,2,0,7,4]
```

 

**提示：**


- ``2 <= n <= 10<sup>4</sup>``
- ``encoded.length == n - 1``
- ``0 <= encoded[i] <= 10<sup>5</sup>``
- ``0 <= first <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/decode-xored-array/)

### 思路及代码

```cpp
class Solution {
public:
    vector<int> decode(vector<int>& encoded, int first) {
        int len = encoded.size();
        vector<int> res(len+1, 0);
        res[0] = first;
        for(int i = 1; i < len+1; i++){
            res[i] = res[i-1] ^ encoded[i-1];
        }
        return res;
    }
};
```