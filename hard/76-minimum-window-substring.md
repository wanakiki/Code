## 76. 最小覆盖子串

2020年5月23日

### 题目

给你一个字符串 S、一个字符串 T，请在字符串 S 里面找出：包含 T 所有字符的最小子串。

**示例：**

```
输入: S = "ADOBECODEBANC", T = "ABC"
输出: "BANC"
```

**说明：**


- 如果 S 中不存这样的子串，则返回空字符串 ``""``。
- 如果 S 中存在这样的子串，我们保证它是唯一的答案。


### 代码

解法可以简单概括为滑动窗加编辑距离。

滑动窗是我一开始想到的办法，但是在这个题目中，窗口被确定后，如何高效的计算窗口中的字母数量是否大于等于字符串T中对应字母数量是一个比较难解决的问题。如果直接遍历判断的话，实际上和暴力没有任何区别。

这里借鉴了官方题解的思路，引入编辑距离量，表示窗口子串和T串之间的区别，如果编辑距离等于T串的长度，则证明窗口中的子串满足题目条件。

在窗口滑动的过程中，编辑距离的更新规则如下：

- 窗口右边界移动，移动前位置对应字母在窗口子串出现次数值小于T串，则编辑距离增加。（如果该字母的数量已经大于等于T中数量，编辑距离不需要改变，但是窗口串字母数量需要正常统计。）
- 窗口左边界移动，移动前位置对应字母在窗口子串出现次数等于T串，编辑距离减一。此时移动会导致窗口子串不满足T串的匹配条件。

剩下的部分就是一些细节问题，具体可以看代码。

```cpp
class Solution {
public:
    string minWindow(string s, string t) {
        // t长度为0
        if(t.size() == 0)   return "";

        int res = INT_MAX;  // 记录长度
        int res_left, res_right;    // 记录最小子串的左右位置
        int cur_left, cur_right;    // 滑动窗口
        int s_freq[128] = {0}, t_freq[128] = {0};   // 记录两个字符串字母出现次数

        // 统计t中字母出现情况
        for(int i = 0; i < t.size(); i++){
            t_freq[t[i]] ++;
        }

        // 窗口滑动
        int distance = 0;   // 编辑距离 
        int t_len = t.size();
        int s_len = s.size();
        cur_left = cur_right = 0;

        while(1){
            
            // 右边界右移
            while(distance != t_len && cur_right < s_len){

                // 只有当前字母出现次数小于t中次数是 distance才需增加
                if(s_freq[s[cur_right]] < t_freq[s[cur_right]]){
                    distance++;
                }

                s_freq[s[cur_right]]++;
                cur_right++;
            }

            // 右移到边界并且字母数量与t不同 直接终止循环
            if(cur_right == s_len && distance != t_len){
                break;
            }

            // 左边界左移
            while(distance == t_len && cur_left < cur_right){

                // 如果左移后字母出现次数小于t 则证明当前为局部最小
                if(s_freq[s[cur_left]] == t_freq[s[cur_left]]){
                    int tmp = cur_right - cur_left;
                    if(tmp < res){
                        res = tmp;
                        res_left = cur_left;
                        res_right = cur_right;
                    }
                    distance--;
                }
                s_freq[s[cur_left]]--;
                cur_left++;
            }
        }
        
        if(res == INT_MAX){
            return "";
        }
        else{
            return s.substr(res_left, res_right-res_left);
        }
    }
};
```