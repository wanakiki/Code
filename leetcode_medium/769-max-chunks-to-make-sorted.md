## 769. 最多能完成排序的块

2022-10-13 19:59:07

### 题目

给定一个长度为 ``n`` 的整数数组 ``arr`` ，它表示在 ``[0, n - 1]`` 范围内的整数的排列。

我们将 ``arr`` 分割成若干 **块** (即分区)，并对每个块单独排序。将它们连接起来后，使得连接的结果和按升序排序后的原数组相同。

返回数组能分成的最多块数量。



**示例 1:**

```
输入: arr = [4,3,2,1,0]
输出: 1
解释:
将数组分成2块或者更多块，都无法得到所需的结果。
例如，分成 [4, 3], [2, 1, 0] 的结果是 [3, 4, 0, 1, 2]，这不是有序的数组。
```

**示例 2:**

```
输入: arr = [1,0,2,3,4]
输出: 4
解释:
我们可以把它分成两块，例如 [1, 0], [2, 3, 4]。
然而，分成 [1, 0], [2], [3], [4] 可以得到最多的块数。
```



**提示:**


- ``n == arr.length``
- ``1 <= n <= 10``
- ``0 <= arr[i] < n``
- ``arr`` 中每个元素都 **不同**



[LeetCode链接](https://leetcode-cn.com/problems/max-chunks-to-make-sorted/)

### 思路及代码

将原数组排序，使用哈希表存储排序后每个数字对应的索引。遍历原数组，记录当前遇到所有元素在排序后数组中最右侧的索引，如果排序后最右侧索引与当前原数组索引重合，则可以进行切分。

```cpp
class Solution {
public:
    int maxChunksToSorted(vector<int>& arr) {
        vector<int> arr_backup(arr.begin(), arr.end());

        sort(arr.begin(), arr.end());
        unordered_map<int, int> hash;
        for(int i = 0; i < arr.size(); i++){
            hash[arr[i]] = i;
        }

        int res = 0;
        int cur_right = 0;
        for(int i = 0; i < arr.size(); i++){
            int tmp = hash[arr_backup[i]];

            cur_right = max(cur_right, tmp);

            if(cur_right == i)  res++;
        }
        return res;
    }
};
```