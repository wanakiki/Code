## 481. 神奇字符串

2022-10-31 10:58:27

### 题目

神奇字符串 ``s`` 仅由 ``'1'`` 和 ``'2'`` 组成，并需要遵守下面的规则：


- 神奇字符串 s 的神奇之处在于，串联字符串中 ``'1'`` 和 ``'2'`` 的连续出现次数可以生成该字符串。


``s`` 的前几个元素是 ``s = "1221121221221121122……"`` 。如果将 ``s`` 中连续的若干 ``1`` 和 ``2`` 进行分组，可以得到 ``"1 22 11 2 1 22 1 22 11 2 11 22 ......"`` 。每组中 ``1`` 或者 ``2`` 的出现次数分别是 ``"1 2 2 1 1 2 1 2 2 1 2 2 ......"`` 。上面的出现次数正是 ``s`` 自身。

给你一个整数 ``n`` ，返回在神奇字符串 ``s`` 的前 ``n`` 个数字中 ``1`` 的数目。

 

**示例 1：**

```
输入：n = 6
输出：3
解释：神奇字符串 s 的前 6 个元素是 “122112”，它包含三个 1，因此返回 3 。 
```

**示例 2：**

```
输入：n = 1
输出：1
```

 

**提示：**


- ``1 <= n <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/magical-string/)

### 思路及代码

使用双指针对字符串进行构造，之后统计 1 的个数。

```cpp
class Solution {
public:
    int magicalString(int n) {
        if(n < 4)   return 1;
        int res = 0;
        vector<int> nums(n, 0);
        nums[0] = 1;
        nums[1] = nums[2] = 2;
        
        int left = 2;
        int right = 3;
        bool flag = true;
        while(right < n){
            if(nums[left] == 1){
                if(flag){
                    nums[right++] = 1;
                }
                else{
                    nums[right++] = 2;
                }
            }
            else{
                if(flag){
                    nums[right++] = 1;
                    if(right < n)   nums[right++] = 1;
                }
                else{
                    nums[right++] = 2;
                    if(right < n)   nums[right++] = 2;
                }
            }
            left++;
            flag = !flag;
        }

        for(int i = 0; i < nums.size(); i++){
            if(nums[i] == 1)    res++;
        }
        return res;
    }
};
```