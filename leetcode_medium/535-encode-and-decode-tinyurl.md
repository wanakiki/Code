## 535. TinyURL 的加密与解密

2022-06-29 09:40:19

### 题目

TinyURL 是一种 URL 简化服务， 比如：当你输入一个 URL ``https://leetcode.com/problems/design-tinyurl`` 时，它将返回一个简化的URL ``http://tinyurl.com/4e9iAk`` 。请你设计一
个类来加密与解密 TinyURL 。

加密和解密算法如何设计和运作是没有限制的，你只需要保证一个 URL 可以被加密成一个 TinyURL ，并且这个 TinyURL 可以用解密方法恢复成原本的 URL 。

实现 ``Solution`` 类：


- ``Solution()`` 初始化 TinyURL 系统对象。
- ``String encode(String longUrl)`` 返回 ``longUrl`` 对应的 TinyURL 。
- ``String decode(String shortUrl)`` 返回 ``shortUrl`` 原本的 URL 。题目数据保证给定的 ``shortUrl`` 是由同一个系统对象加密的。




**示例：**

```
输入：url = "https://leetcode.com/problems/design-tinyurl"
输出："https://leetcode.com/problems/design-tinyurl"

解释：
Solution obj = new Solution();
string tiny = obj.encode(url); // 返回加密后得到的 TinyURL 。
string ans = obj.decode(tiny); // 返回解密后得到的原本的 URL 。
```



**提示：**


- ``1 <= url.length <= 10<sup>4</sup>``
- 题目数据保证 ``url`` 是一个有效的 URL




[LeetCode链接](https://leetcode-cn.com/problems/encode-and-decode-tinyurl/)


### 思路及代码

自增id做法。

```cpp
class Solution {
public:
    int id;
    unordered_map<int, string> hash;
    Solution(){
        id = 0;
    }
    // Encodes a URL to a shortened URL.
    string encode(string longUrl) {
        hash[id] = longUrl;
        string res = "http://tinyurl.com/" + to_string(id++);
        return res;
    }

    // Decodes a shortened URL to its original URL.
    string decode(string shortUrl) {
        string num = shortUrl.substr(19);
        int tmp = stoi(num);
        return hash[tmp];
    }
};

// Your Solution object will be instantiated and called as such:
// Solution solution;
// solution.decode(solution.encode(url));
```


其他可采用的做法是随机数和直接哈希生成。