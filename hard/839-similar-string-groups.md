## 869. 相似字符串组

2021-01-31 17:10:23

### 题目

如果交换字符串 ``X`` 中的两个不同位置的字母，使得它和字符串 ``Y`` 相等，那么称 ``X`` 和 ``Y`` 两个字符串相似。如果这两个字符串本身是相等的，那它们也是相似的。

例如，``"tars"`` 和 ``"rats"`` 是相似的 (交换 ``0`` 与 ``2`` 的位置)； ``"rats"`` 和 ``"arts"`` 也是相似的，但是 ``"star"`` 不与 ``"tars"``，``"rats"``，或 ``"arts"`` 相似。

总之，它们通过相似性形成了两个关联组：``{"tars", "rats", "arts"}`` 和 ``{"star"}``。注意，``"tars"`` 和 ``"arts"`` 是在同一组中，即使它们并不相似。形式上，对每个组而言，要确定一个单词在组中，只需要这个词和该组中至少一个单词相似。

给你一个字符串列表 ``strs``。列表中的每个字符串都是 ``strs`` 中其它所有字符串的一个字母异位词。请问 ``strs`` 中有多少个相似字符串组？

 

**示例 1：**

```
输入：strs = ["tars","rats","arts","star"]
输出：2
```

**示例 2：**

```
输入：strs = ["omv","ovm"]
输出：1
```

 

**提示：**


- ``1 <= strs.length <= 100``
- ``1 <= strs[i].length <= 1000``
- ``sum(strs[i].length) <= 2 * 10<sup>4</sup>``
- ``strs[i]`` 只包含小写字母。
- ``strs`` 中的所有单词都具有相同的长度，且是彼此的字母异位词。


 

**备注：**

字母异位词（anagram），一种把某个字符串的字母的位置（顺序）加以改换所形成的新词。


[LeetCode链接](https://leetcode-cn.com/problems/similar-string-groups/)    

### 思路及代码

提议理解起来比较难，字符串之间的相似关系可以让彼此建立起联系，例如：a与b相似，b与c相似，虽然a与c实际上不相似，但是由于b这个桥梁，a、b、c三者会处在一个相似组中。题目的目的也就是让我们求类似的相似组的个数，比较容易想到用并查集来解决问题。

```cpp
class UnionFind {
public:
    vector<int> parent;
    int count;
    int n;
    UnionFind(int _n) : parent(_n), count(_n), n(_n){
        for(int i = 0; i < parent.size(); i++){
            parent[i] = i;
        }
    }
    int findx(int x){
        if(x != parent[x]){
            parent[x] = findx(parent[x]);
        }
        return parent[x];
    }
    bool merge(int x, int y){
        int a = findx(x);
        int b = findx(y);
        if(a == b){
            return false;
        }
        else{
            parent[b] = a;
            count--;
            return true;
        }
    }
};
class Solution {
public:
    // 判断两个字符串是否相似
    bool helper2(string x, string y){
        if(x.size() != y.size()){
            return false;
        }
        
        int last_index = -1;
        for(int i = 0; i < x.size(); i++){
            if(x[i] != y[i]){
                if(last_index == -1){
                    last_index = i;
                }
                else if(last_index == -2){
                    return false;
                }
                else{
                    if(x[last_index] == y[i] && y[last_index] == x[i]){
                        last_index = -2;
                    }
                    else{
                        return false;
                    }
                }
            }
        }
        return true;
    }
    int numSimilarGroups(vector<string>& strs) {
        int len = strs.size();
        UnionFind uf(len);
        // 判断任意两个字符串是否相似
        for(int i = 0; i < len; i++){
            for(int j = i + 1; j < len; j++){
                if(helper(strs[i], strs[j])){
                    uf.merge(i, j);
                }
            }
        }
        return uf.count;
    }
};
```