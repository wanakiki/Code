## 剑指Offer 114.外星文字典

2022-05-31 19:30:41

### 题目

现有一种使用英语字母的外星文语言，这门语言的字母顺序与英语顺序不同。

给定一个字符串列表 ``words`` ，作为这门语言的词典，``words`` 中的字符串已经 **按这门新语言的字母顺序进行了排序** 。

请你根据该词典还原出此语言中已知的字母顺序，并 **按字母递增顺序** 排列。若不存在合法字母顺序，返回 ``""`` 。若存在多种可能的合法字母顺序，返回其中 **任意一种** 顺序即可。

字符串 ``s`` **字典顺序小于** 字符串 ``t`` 有两种情况：


- 在第一个不同字母处，如果 ``s`` 中的字母在这门外星语言的字母顺序中位于 ``t`` 中字母之前，那么 ``s`` 的字典顺序小于 ``t`` 。
- 如果前面 ``min(s.length, t.length)`` 字母都相同，那么 ``s.length < t.length`` 时，``s`` 的字典顺序也小于 ``t`` 。




**示例 1：**

```
输入：words = ["wrt","wrf","er","ett","rftt"]
输出："wertf"
```

**示例 2：**

```
输入：words = ["z","x"]
输出："zx"
```

**示例 3：**

```
输入：words = ["z","x","z"]
输出：""
解释：不存在合法字母顺序，因此返回 "" 。
```



**提示：**


- ``1 <= words.length <= 100``
- ``1 <= words[i].length <= 100``
- ``words[i]`` 仅由小写英文字母组成




<meta charset="UTF-8" />注意：本题与主站 269 题相同： <a href="https://leetcode-cn.com/problems/alien-dictionary/">https://leetcode-cn.com/problems/alien-dictionary/</a>


[LeetCode链接](https://leetcode-cn.com/problems/Jf1JuT/)

### 思路及代码

题目主要思路是根据排序后的字符串列表得到字母之间的大小关系，可构成有向图。接着查看能否对有向图进行拓扑排序，如果有环则返回空，否则返回拓扑排序结果。

实现代码时发现有较多的量需要统计，需要避免对相同的边进行重复记录，并且需要排除 ``abc ab`` 这样的错误数据。整体难度不是很高，但写起来不是很流畅。

```cpp
class Solution {
public:
    string alienOrder(vector<string>& words) {
        // 有向图判断是否有环
        vector<vector<bool>> graph(26, vector<bool>(26, false));
        vector<bool> appear(26, false);
        vector<int> count(26, 0);   // 统计入度
        
        for(int j = 0; j < words.size(); j++){
            string s = words[j];
            for(int i = 0; i < s.size(); i++){
                appear[s[i] - 'a'] = true;
            }
        }
        for(int i = 1; i < words.size(); i++){
            // 比较当前元素和前一个元素
            for(int j = 0; j < words[i-1].size(); j++){
                if(j >= words[i].size())    return "";  // abc ab 直接判错
                if(words[i][j] != words[i-1][j]){

                    // 此处应避免重复记录边 ！
                    if(!graph[words[i-1][j] - 'a'][words[i][j] - 'a']){
                        graph[words[i-1][j] - 'a'][words[i][j] - 'a'] = true;
                        count[words[i][j] - 'a']++;
                    }
                    
                    break;
                }
            }
        }

        // 根据图判断是否有环
        string res = "";

        // 开始搜索记录路径
        while(1){
            bool flag = false;
            for(int i = 0; i < appear.size(); i++){
                if(appear[i] && count[i] == 0){
                    flag = true;
                    res += string(1, i + 'a');
                    appear[i] = false;
                    for(int j = 0; j < 26; j++){
                        if(graph[i][j]){
                            count[j]--;
                        }
                    }
                    //cout << char(i + 'a') << endl;
                }
            }
            if(!flag)   break;
        }

        // 如果仍有字符 则意味着存在环
        for(int i = 0; i < appear.size(); i++){
            if(appear[i])   return "";
        }
        return res;
    }
};
```