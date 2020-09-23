## 846. 一手顺子

2020年9月23日

### 题目

爱丽丝有一手（``hand``）由整数数组给定的牌。 

现在她想把牌重新排列成组，使得每个组的大小都是 ``W``，且由 ``W`` 张连续的牌组成。

如果她可以完成分组就返回 ``true``，否则返回 ``false``。

 




**示例 1：**

```
输入：hand = [1,2,3,6,2,3,4,7,8], W = 3
输出：true
解释：爱丽丝的手牌可以被重新排列为 [1,2,3]，[2,3,4]，[6,7,8]。```

**示例 2：**

```
输入：hand = [1,2,3,4,5], W = 4
输出：false
解释：爱丽丝的手牌无法被重新排列成几个大小为 4 的组。```

 

**提示：**


- ``1 <= hand.length <= 10000``
- ``0 <= hand[i] <= 10^9``
- ``1 <= W <= hand.length``


 

**注意：**此题目与 1294 重复：<a href="https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/" target="_blank">https://leetcode-cn.com/problems/divide-array-in-sets-of-k-consecutive-numbers/</a>



### 思路及代码

首先，如果牌数不能被W除尽，则必然不满足条件。

在此基础之上，将数组排序，并统计每个数出现的次数。之后从最小的元素开始，模拟整个组牌的过程。如果达不到窗长、相邻数字只差不为1、或者后面的元素出现次数小于初始元素这三种情况的任何一种，则证明不能够成功组牌。


```cpp
class Solution {
public:
    bool isNStraightHand(vector<int>& hand, int W) {
        if(hand.size() % W){
            return false;
        }
        sort(hand.begin(), hand.end());

        int nums[10005][2];
        int index = 0;
        nums[index][0] = hand[0];
        nums[index][1] = 1;
        for(int i = 1; i < hand.size(); i++){
            if(hand[i] == nums[index][0]){
                nums[index][1]++;
            }
            else{
                index++;
                nums[index][0] = hand[i];
                nums[index][1] = 1;
            }
        }

        // 开始遍历
        int count = index+1;    // 注意上面的循环结束后 index指向的位置有值
        index = 0;
        while(1){
            int cur = nums[index][1];   // 首个数字出现次数
            nums[index][1] = 0;
            for(int i = index + 1; i < index + W; i++){
                if(i == count || nums[i][0] != nums[i-1][0]+1 || nums[i][1] < cur){
                    return false;
                }
                else{
                    nums[i][1] -= cur;
                }
            }

            // 找到下一个剩余次数不为零的点
            for(;index < count; index++){
                if(nums[index][1] != 0){
                    break;
                }
            }
            if(index == count){
                break;
            }
        }

        return true;
    }
};
```