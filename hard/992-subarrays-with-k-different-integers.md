## 1034. K 个不同整数的子数组

2021-02-09 11:58:00

### 题目

给定一个正整数数组 ``A``，如果 ``A`` 的某个子数组中不同整数的个数恰好为 ``K``，则称 ``A`` 的这个连续、不一定独立的子数组为<em>好子数组</em>。

（例如，``[1,2,3,1,2]`` 中有 ``3`` 个不同的整数：``1``，``2``，以及 ``3``。）

返回 ``A`` 中<em>好子数组</em>的数目。

 

**示例 1：**

```
输入：A = [1,2,1,2,3], K = 2
输出：7
解释：恰好由 2 个不同整数组成的子数组：[1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2].
```

**示例 2：**

```
输入：A = [1,2,1,3,4], K = 3
输出：3
解释：恰好由 3 个不同整数组成的子数组：[1,2,1,3], [2,1,3], [1,3,4].
```

 

**提示：**


- ``1 <= A.length <= 20000``
- ``1 <= A[i] <= A.length``
- ``1 <= K <= A.length``



[LeetCode链接](https://leetcode-cn.com/problems/subarrays-with-k-different-integers/)

### 思路及代码

采用滑动窗口思想，不断扩大窗口长度直到不同整数个数为K，此时向右移动左端点，找到过程中整数个数仍为K的子数组个数。当扩展窗口长度后，整数类型数超过K时，则应移动左端点，直到变为K。

```cpp
class Solution {
   public:
    int subarraysWithKDistinct(vector<int>& A, int K) {
        // 滑动窗口向右扩展长度
        // 小于K长度继续扩展，大于K左边界向右移动
        // 直到独立数为K-1；等于K尝试移动左节点 直到不满足个数为K停止
        // 重复上述过程 并记录独立数为K的情况

        unordered_map<int, int> count;
        int sum = 0;  // 独立数个数
        int left = 0, right = 0;
        int res = 0;
        while (right < A.size()) {
            if (count.find(A[right]) == count.end() || count[A[right]] == 0) {
                sum++;
            }
            count[A[right++]] += 1;

            // 当个数大于K时
            if (sum > K) {
                while (left < right) {
                    if (count[A[left]] == 1) {
                        sum--;
                    }
                    count[A[left++]]--;
                    if (sum == K) {
                        break;
                    }
                }
            }

            // 个数大于K后调整左端点 之后个数等于K同样需要进行个数判断
            if (sum == K) {
                int tmp = left;  // 移动左端点
                while (left <= right) {
                    res++;
                    // 一直移动 遇到第一个个数为1的数时停止
                    if (count[A[left]] == 1) {
                        left--;
                        break;
                    }
                    count[A[left]]--;
                    left++;
                }

                // 复位左端点
                while (left >= tmp) {
                    count[A[left]]++;
                    left--;
                }
                left = tmp;
            }
        }
        return res;
    }
};
```

上面算法比较复杂的点在于每次移动左端点之后都要对左端点的位置进行还原，存在较多重复计算。官方题解给出的做法是维护两个左端点，分别对应整数个数为K和K-1两种情况，这样对于任意右端点可以直接计算出可能的子数组个数。