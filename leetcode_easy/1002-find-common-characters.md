## 1002. 查找常用字符

2020年10月14日

### 题目

给定仅有小写字母组成的字符串数组 ``A``，返回列表中的每个字符串中都显示的全 
部字符（**包括重复字符**）组成的列表。例如，如果一个字符在每个字符串中出现 
3 次，但不是 4 次，则需要在最终答案中包含该字符 3 次。

你可以按任意顺序返回答案。



**示例 1：**

```
输入：["bella","label","roller"]
输出：["e","l","l"]
```

**示例 2：**

```
输入：["cool","lock","cook"]
输出：["c","o"]
```



**提示：**


- ``1 <= A.length <= 100``
- ``1 <= A[i].length <= 100``
- ``A[i][j]`` 是小写字母

### 思路及代码

用一个数组保存每个字母出现的最小频率，然后遍历每个字符串，统计字母出现的次数，最后逐个与结果数组相比较，保留较小的值。

另外，新建string的方式是，string(n, 'a')，n是长度，'a'是需要重复的字符。

```cpp
class Solution {
public:
    vector<string> commonChars(vector<string>& A) {
        
        vector<int> res(128, INT_MAX);
        for(int i = 0; i < A.size(); i++){
            vector<int> count(128, 0);
            for(int j = 0; j < A[i].size(); j++){
                count[A[i][j]]++;
            }
            for(int i = 'a'; i <= 'z'; i++){
                res[i] = min(res[i], count[i]);
            }
        }
        vector<string> ress;
        for(int i = 'a'; i <= 'z'; i++){
            int n = res[i];
            while(n--){
                ress.emplace_back(string(1, i));    // 注意创建string
            }
        }
        return ress;
    }
};
```