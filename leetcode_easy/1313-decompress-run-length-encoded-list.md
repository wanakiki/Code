## 1313. 解压缩编码列表

2021-09-04 16:33:34

### 题目

给你一个以行程长度编码压缩的整数列表 ``nums`` 。

考虑每对相邻的两个元素 ``[freq, val] = [nums[2*i], nums[2*i+1]]`` （其中 ``i >= 0`` ），每一对都表示解压后子列表中有 ``freq`` 个值为 ``val`` 的元素， 
你需要从左到右连接所有子列表以生成解压后的列表。

请你返回解压后的列表。

 

**示例 1：**

```
输入：nums = [1,2,3,4]
输出：[2,4,4,4]
解释：第一对 [1,2] 代表着 2 的出现频次为 1，所以生成数组 [2]。
第二对 [3,4] 代表着 4 的出现频次为 3，所以生成数组 [4,4,4]。
最后将它们串联到一起 [2] + [4,4,4] = [2,4,4,4]。
```

**示例 2：**

```
输入：nums = [1,1,2,3]
输出：[1,3,3]
```

 

**提示：**


- ``2 <= nums.length <= 100``
- ``nums.length % 2 == 0``
- ``1 <= nums[i] <= 100``



[LeetCode链接](https://leetcode-cn.com/problems/decompress-run-length-encoded-list/)

### 思路及代码

```cpp
class Solution {
public:
    vector<int> decompressRLElist(vector<int>& nums) {
        vector<int> res;
        for(int i = 0; i < nums.size(); i+=2){
            int freq = nums[i];
            int num = nums[i+1];

            //vector<int> tmp(freq, num);
            //res.insert(res.end(), tmp.begin(), tmp.end()); 这种写法最慢且傻

            // res.insert(res.end(), freq, num);
            
            for(int j = 0; j < freq; j++){
                res.push_back(num);
            }
        }
        return res;
    }
};
```