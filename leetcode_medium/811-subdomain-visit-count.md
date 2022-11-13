## 811. 子域名访问计数

2022-10-05 09:33:45

### 题目

网站域名 ``"discuss.leetcode.com"`` 由多个子域名组成。顶级域名为 ``"com"`` ，二级域名为 ``"leetcode.com"`` ，最低一级为 ``"discuss.leetcode.com"`` 。当访问域名 ``"discuss.leetcode.com"`` 时，同时也会隐式访问其父域名 ``"leetcode.com" ``以及 ``"com"`` 。

**计数配对域名** 是遵循 ``"rep d1.d2.d3"`` 或 ``"rep d1.d2"`` 格式的一个域名表示，其中 ``rep`` 表示访问域名的次数，``d1.d2.d3`` 为域名本身。


- 例如，``"9001 discuss.leetcode.com"`` 就是一个 **计数配对域名** ，表示 ``discuss.leetcode.com`` 被访问了 ``9001`` 次。


给你一个**计数配对域名**组成的数组 ``cpdomains`` ，解析得到输入中每个子域名对应的 **计数配对域名** ，并以数组形式返回。可以按 **任意顺序** 返回答案。



**示例 1：**

```
输入：cpdomains = ["9001 discuss.leetcode.com"]
输出：["9001 leetcode.com","9001 discuss.leetcode.com","9001 com"]
解释：例子中仅包含一个网站域名："discuss.leetcode.com"。
按照前文描述，子域名 "leetcode.com" 和 "com" 都会被访问，所以它们都被访问了 9001 次。
```

**示例 2：**

```
输入：cpdomains = ["900 google.mail.com", "50 yahoo.com", "1 intel.mail.com", "5 wiki.org"]
输出：["901 mail.com","50 yahoo.com","900 google.mail.com","5 wiki.org","5 org","1 intel.mail.com","951 com"]
解释：按照前文描述，会访问 "google.mail.com" 900 次，"yahoo.com" 50 次，"intel.mail.com" 1 次，"wiki.org" 5 次。
而对于父域名，会访问 "mail.com" 900 + 1 = 901 次，"com" 900 + 50 + 1 = 951 次，和 "org" 5 次。
```



**提示：**


- ``1 <= cpdomain.length <= 100``
- ``1 <= cpdomain[i].length <= 100``
- ``cpdomain[i]`` 会遵循 ``"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>.d3<sub>i</sub>"`` 或 ``"rep<sub>i</sub> d1<sub>i</sub>.d2<sub>i</sub>"`` 格式
- ``rep<sub>i</sub>`` 是范围 ``[1, 10<sup>4</sup>]`` 内的一个整数
- ``d1<sub>i</sub>``、``d2<sub>i</sub>`` 和 ``d3<sub>i</sub>`` 由小写英文字母组成



[LeetCode链接](https://leetcode-cn.com/problems/subdomain-visit-count/)

### 思路及代码

使用哈希表对每个子域名出现次数进行计数，遍历哈希表并合成目标格式的字符串。对于给定的输入，可以首先查找空格找到请求次数，接着逐个查找 ``.`` 的位置，并生成子串计数。

```cpp
class Solution {
public:
    vector<string> subdomainVisits(vector<string>& cpdomains) {
        vector<string> res;
        
        unordered_map<string, int> hash;
        
        for(auto cpdomain : cpdomains){
            int space_index = cpdomain.find(' ');
            int count = stoi(cpdomain.substr(0, space_index));

            cpdomain = cpdomain.substr(space_index + 1);
            hash[cpdomain] += count;
            for(int i = 1; i < cpdomain.size(); i++){
                if(cpdomain[i] == '.'){
                    hash[cpdomain.substr(i + 1)] += count;
                }
            }
        }

        for(auto it = hash.begin(); it != hash.end(); it++){
            res.push_back(to_string(it->second) + " " + it->first);
        }
        return res;
    }
};
```