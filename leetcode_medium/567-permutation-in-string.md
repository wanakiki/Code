## 567. 字符串的排列

2021-02-10 13:01:14

### 题目

给定两个字符串 **s1** 和 **s2**，写一个函数来判断 **s2** 是否包含 **s1**的排列。

换句话说，第一个字符串的排列之一是第二个字符串的子串。

**示例1:**

```
输入: s1 = "ab" s2 = "eidbaooo"
输出: True
解释: s2 包含 s1 的排列之一 ("ba").
```

 

**示例2:**

```
输入: s1= "ab" s2 = "eidboaoo"
输出: False
```


**注意：**


- 输入的字符串只包含小写字母
- 两个字符串的长度都在 [1, 10,000] 之间



[LeetCode链接](https://leetcode-cn.com/problems/permutation-in-string/)

### 思路及代码

根据题意比较容易想到用滑动窗口来做，窗口长度为s1长度，若当前窗口有不满足条件的字母则向后移动。对于窗内任意字母可能有三种情况：

1. 出现次数等于s1中出现次数，该字母正常
2. 出现次数小于s1中出现次数，当前窗不满足要求需要向后滑动
3. 出现次数大于s1中出现次数，当前窗不满足要求需要向后滑动

由于窗长度固定，所以2、3两种情况必然会同时出现，为了在不考虑窗口滑动之后各字母出现次数的前提下获得最大的滑动距离，应该选用位于最右侧出现次数大于s1中出现次数的字母。

```cpp
class Solution {
public:
    bool checkInclusion(string s1, string s2) {
        // 窗长为s1长度
        // 发现不在s1中的字母之后重置所有窗口长度
        // 过程中发现有某个字符个数超标需要移动整个窗口 移动后需要检查是否有字符超标判断是否要继续移动

        if(s1.size() > s2.size()){
            return false;
        }
        vector<int> count_1(26, 0);
        vector<int> count_2(26, 0);

        for(auto c : s1){
            count_1[c - 'a']++;
        }
        int len = s1.size();

        for(int i = 0; i < len; i++){
            count_2[s2[i] - 'a']++;
        }
        int left = 0, right = len-1;
        while(right < s2.size()){
            // 检查是否满足 统计最长移动距离
            // 次数相等则跳过 不足不需要考虑(长度固定 有不足则必有多余) 超过则应移动
            vector<int> flag(26, 0);    // 统计需要删除的个数
            int next_left = left;
            for(int i = left; i <= right; i++){
                int cur = s2[i] - 'a';
                if(count_2[cur] - flag[cur] > count_1[cur]){
                    flag[cur]++;
                    next_left = i + 1;
                }
            }

            if(next_left == left){
                return true;
            }
            else{
                cout << next_left << endl;
                int next_right = next_left - left + right;
                if(next_right >= s2.size()){
                    return false;
                }
                for(int i = left; i < next_left; i++){
                    int cur = s2[i] - 'a';
                    count_2[cur]--;
                    right++;
                    count_2[s2[right] - 'a']++;
                }
                left = next_left;
            }
        }
        return false;
    }
};
```

但上面的做法运行起来稍慢，官方题解给到了一个不错的思路：采用双指针做法，用一个长度为26的数组A代表s1与s2指针范围内字符串的差异，初始值为s1中各个字母的出现次数，接着遍历s2，根据s2当前遍历到的字母使A中对应位置减一。目标是使A中各位置均为零，即差异为零。