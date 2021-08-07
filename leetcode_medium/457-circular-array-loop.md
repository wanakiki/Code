## 457. 环形数组是否存在循环

2021-08-07 18:48:30

### 题目

存在一个不含 ``0`` 的 **环形** 数组 ``nums`` ，每个 ``nums[i]`` 都表示位于下标 ``i`` 的角色应该向前或向后移动的下标个数：


- 如果 ``nums[i]`` 是正数，**向前** 移动 ``nums[i]`` 步
- 如果 ``nums[i]`` 是负数，**向后** 移动 ``nums[i]`` 步


因为数组是 **环形** 的，所以可以假设从最后一个元素向前移动一步会到达第一个元素，而第一个元素向后移动一步会到达最后一个元素。

数组中的 **循环** 由长度为 ``k`` 的下标序列 ``seq`` ：


- 遵循上述移动规则将导致重复下标序列 ``seq[0] -> seq[1] -> ... -> seq[k - 1] -> seq[0] -> ...``
- 所有 ``nums[seq[j]]`` 应当不是 **全正** 就是 **全负**
- ``k > 1``


如果 ``nums`` 中存在循环，返回 ``true`` ；否则，返回``false``。

 

**示例 1：**

```
输入：nums = [2,-1,1,2,2]
输出：true
解释：存在循环，按下标 0 -> 2 -> 3 -> 0 。循环长度为 3 。
```

**示例 2：**

```
输入：nums = [-1,2]
输出：false
解释：按下标 1 -> 1 -> 1 ... 的运动无法构成循环，因为循环的长度为 1 。根据定义，循环的长度必须大于 1 。
```

**示例 3:**

```

输入：nums = [-2,1,-1,-2,-2]
输出：false
解释：按下标 1 -> 2 -> 1 -> ... 的运动无法构成循环，因为 nums[1] 是正数，而 nums[2] 是负数。
所有 nums[seq[j]] 应当不是全正就是全负。
```

 

**提示：**


- ``1 <= nums.length <= 5000``
- ``-1000 <= nums[i] <= 1000``
- ``nums[i] != 0``


 

**进阶：** 你能设计一个时间复杂度为 ``O(n)`` 且额外空间复杂度为 ``O(1)`` 的算法吗？


[LeetCode链接](https://leetcode-cn.com/problems/circular-array-loop/)

### 思路及代码

数组给定之后每个节点所在的路径是固定的，可以通过扫描数组得到路径信息。通常情况下会使用额外空间保存状态，但是对于本题而言，考虑到数据范围，可以采取原地存储方法，达到节省空间的目的。

在代码中，使用一个大于5000的数据作为轮次标记，在数组中遍历时遇到相同轮次时便可判断数据是否成环。需要注意处理完一条路径之后该值加一，以区分不同路径。

另外，针对于单节点成环的情况需要特殊处理。

```cpp
class Solution {
public:
    bool circularArrayLoop(vector<int>& nums) {
        int flag  = 6000;
        int n = nums.size();
        for(int i = 0; i < nums.size(); i++){
            if(nums[i] >= 6000) continue;   // 已经处理过则跳过

            int cur = ((i + nums[i]) % n + n) % n;
            bool direction = nums[i] > 0;   // nums[i]不为零
            int count = 1;
            nums[i] = flag;

            while(1){
                if(nums[cur] >= 6000){
                    // 遇到标记节点 如果与当前不是同一轮次则终止当前轮次
                    if(nums[cur] == flag && count > 1)    return true;
                    else    break;
                }

                // 如果符号不同 终止循环，无需标记
                if(direction != (nums[cur] > 0))    break;

                int tmp = cur;
                cur = ((cur + nums[cur]) % n + n) % n;
                nums[tmp] = flag;
                count++;
                // 提前处理单节点成环的情况
                if(cur == tmp) break;
            }
            flag++;
        }
        return false;
    }
};
```