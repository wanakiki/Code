## 1574. 删除最短的子数组使剩余数组有序

2023-03-25 16:09:29

### 题目

给你一个整数数组 ``arr`` ，请你删除一个子数组（可以为空），使得 ``arr`` 中剩下的元素是 **非递减** 的。

一个子数组指的是原数组中连续的一个子序列。

请你返回满足题目要求的最短子数组的长度。

 

**示例 1：**

```

输入：arr = [1,2,3,10,4,2,3,5]
输出：3
解释：我们需要删除的最短子数组是 [10,4,2] ，长度为 3 。剩余元素形成非递减数组 [1,2,3,3,5] 。
另一个正确的解为删除子数组 [3,10,4] 。
```

**示例 2：**

```

输入：arr = [5,4,3,2,1]
输出：4
解释：由于数组是严格递减的，我们只能保留一个元素。所以我们需要删除长度为 4 的子数组，要么删除 [5,4,3,2]，要么删除 [4,3,2,1]。
```

**示例 3：**

```

输入：arr = [1,2,3]
输出：0
解释：数组已经是非递减的了，我们不需要删除任何元素。
```

**示例 4：**

```

输入：arr = [1]
输出：0
```

 

**提示：**


- ``1 <= arr.length <= 10^5``
- ``0 <= arr[i] <= 10^9``



[LeetCode链接](https://leetcode-cn.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/)

### 思路及代码

个人感觉是一个比较不错的题目，读完题需要思考一下才能想到做法。由于被删除的数组是连续的，一共会有三种情况：
- 被删除的数组在末尾
- 在开始
- 在中间

需要在原始数组中分别在开始和结尾找到最长的非递减数组，如果两个数组长度和大于原始数组长度，说明整个数组非递减。否则，可以直接计算出删除的数组在开始和末尾的情况，接着使用双指针计算被删除的数组在中间的情况。

```cpp
class Solution {
public:
    int findLengthOfShortestSubarray(vector<int>& arr) {
        int left_count = 1;
        int right_count = 1;
        
        for(int i = 1; i < arr.size(); i++){
            if(arr[i] >= arr[i-1]){
                left_count++;
            }
            else{
                break;
            }
        }

        for(int i = arr.size() - 2; i >= 0; i--){
            if(arr[i+1] >= arr[i]){
                right_count++;
            }
            else{
                break;
            }
        }

        // 判断是否整体递增
        int len = arr.size();
        if(left_count + right_count > len)  return 0;

        int res = min(len - left_count, len - right_count);

        // 双指针查找两侧能组成的最长序列
        // left和right分别指向前后缀最开始的位置，之后针对于left找到第一个满足条件的right，之后left移动，此时right只需要继续向后移动
        // 重复这个过程直到有一个指针到达了端点
        int left = 0;
        int right = len - right_count;
        while(left < left_count){
            while(right < len && arr[left] > arr[right]){
                right++;
            }
            if(right == len)    break;
            res = min(res, len - (left + 1) - (len - right));
            left++;
        }
        return res;
    }
};
```
