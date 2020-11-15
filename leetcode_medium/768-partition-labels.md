## 768. 划分字母区间

2020-11-15 17:17:12

### 题目

字符串 ``S`` 由小写字母组成。我们要把这个字符串划分为尽可能多的片段，同一字母最多出现在一个片段中。返回一个表示每个字符串 
片段的长度的列表。

 

**示例：**

```
输入：S = "ababcbacadefegdehijhklij"
输出：[9,7,8]
解释：
划分结果为 "ababcbaca", "defegde", "hijhklij"。
每个字母最多出现在一个片段中。
像 "ababcbacadefegde", "hijhklij" 的划分是错误的，因为划分的片段数较少。
```

 

**提示：**


- ``S``的长度在``[1, 500]``之间。
- ``S``只包含小写字母 ``'a'`` 到 ``'z'`` 。



### 思路及代码

遍历字符串统计每个字符的起始位置，之后从第一个字符开始遍历，遍历区间内的所有字符，遇到新的字符之后更新右侧区间长度。更新结束之后计算区间长度并存储。

```cpp
class Solution {
public:
    vector<int> partitionLabels(string S) {
        vector<vector<int>> intervals(26, vector<int>(2, -1));
        for(int i = 0; i < S.size(); i++){
            int tmp = S[i] - 'a';
            if(intervals[tmp][0] == -1){
                intervals[tmp][0] = i;
            }
            intervals[tmp][1] = i;
        }

        int cur = 0;
        vector<int> res;
        while(cur < S.size()){
            int right = intervals[S[cur] - 'a'][1];
            int start = cur;
            while(cur < right){
                cur++;
                right = max(right, intervals[S[cur] - 'a'][1]);   
            }
            res.push_back(cur - start + 1);
            cur++;
        }
        return res;
    }
};
```

实际上统计每个字符出现的收个位置是不必须的。