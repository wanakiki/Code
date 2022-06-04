## 953. 验证外星语词典

2022-05-17 21:34:54

### 题目

某种外星语也使用英文小写字母，但可能顺序 ``order`` 不同。字母表的顺序（``order``）是一些小写字母的排列。

给定一组用外星语书写的单词 ``words``，以及其字母表的顺序 ``order``，只有当给定的单词在这种外星语中按字典序排列时，返回 ``true``；否则，返回 ``false``。

 

**示例 1：**

```
输入：words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
输出：true
解释：在该语言的字母表中，'h' 位于 'l' 之前，所以单词序列是按字典序排列的。
```

**示例 2：**

```
输入：words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
输出：false
解释：在该语言的字母表中，'d' 位于 'l' 之后，那么 words[0] > words[1]，因此单词序列不是按字典序排列的。
```

**示例 3：**

```
输入：words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
输出：false
解释：当前三个字符 "app" 匹配时，第二个字符串相对短一些，然后根据词典编纂规则 "apple" > "app"，因为 'l' > '∅'，其中 '∅' 是空白字符，定义为比任何其他字符都小（<a href="https://baike.baidu.com/item/%E5%AD%97%E5%85%B8%E5%BA%8F" target="_blank">更多信息）。

```

 

**提示：**


- ``1 <= words.length <= 100``
- ``1 <= words[i].length <= 20``
- ``order.length == 26``
- 在 ``words[i]`` 和 ``order`` 中的所有字符都是英文小写字母。



[LeetCode链接](https://leetcode-cn.com/problems/verifying-an-alien-dictionary/)

### 思路及代码

遍历数组中的字符串，将其与之前的字符串进行比较。

```cpp
class Solution {
public:
    bool isAlienSorted(vector<string>& words, string order) {

        unordered_map<int,int> hash;
        for(int i = 0; i < order.size(); i++){
            hash[order[i]] = i;
        }

        for(int i = 1; i < words.size(); i++){

            int len_a = words[i].size();
            int len_b = words[i-1].size();

            int index = 0;
            while(index < min(len_a, len_b)){
                if(hash[words[i][index]] < hash[words[i-1][index]]){
                    return false;
                }
                else if(hash[words[i][index]] > hash[words[i-1][index]]){
                    break;
                }
                index++;
            }
            if(index == min(len_a, len_b) && len_b > len_a)   return false;     // 遍历完所有的字符串之后根据长度比较大小
        }
        return true;
    }
};
```