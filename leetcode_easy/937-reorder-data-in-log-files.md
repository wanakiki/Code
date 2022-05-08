## 974. 重新排列日志文件

2022-05-03 20:00:19

### 题目

给你一个日志数组 ``logs``。每条日志都是以空格分隔的字串，其第一个字为字母与数字混合的 **标识符**。

有两种不同类型的日志：


- **字母日志**：除标识符之外，所有字均由小写字母组成
- **数字日志**：除标识符之外，所有字均由数字组成


请按下述规则将日志重新排序：


- 所有 **字母日志** 都排在 **数字日志** 之前。
- **字母日志** 在内容不同时，忽略标识符后，按内容字母顺序排序；在内容相同时，按标识符排序。
- **数字日志** 应该保留原来的相对顺序。


返回日志的最终顺序。

 

**示例 1：**

```
输入：logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
输出：["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]
解释：
字母日志的内容都不同，所以顺序为 "art can", "art zero", "own kit dig" 。
数字日志保留原来的相对顺序 "dig1 8 1 5 1", "dig2 3 6" 。
```

**示例 2：**

```
输入：logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
输出：["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
```

 

**提示：**


- ``1 <= logs.length <= 100``
- ``3 <= logs[i].length <= 100``
- ``logs[i]`` 中，字与字之间都用 **单个** 空格分隔
- 题目数据保证 ``logs[i]`` 都有一个标识符，并且在标识符之后至少存在一个字



[LeetCode链接](https://leetcode-cn.com/problems/reorder-data-in-log-files/)

### 思路及代码

题目考察对字符串的自定义排序，由题目要求可知，数字类型的日志文件不参与排序，因此可以遍历一次数组，将两种类型的日志分别保存。对字母日志单独排序之后将数字日志拼接到数组末尾。

```cpp
class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        vector<string> num_log;
        vector<string> chara_log;

        for(int i = 0; i < logs.size(); i++){
            // 判断最后一个字符是否为数字
            int index = logs[i].size() - 1;
            if('0' <= logs[i][index] && logs[i][index] <= '9'){
                num_log.push_back(logs[i]);
            }
            else{
                chara_log.push_back(logs[i]);
            }
        }


        // 对字母日志进行排序
        sort(chara_log.begin(), chara_log.end(), [&](const string& log_a, const string& log_b){
            int index_a = 0;
            int index_b = 0;
            while(log_a[index_a] != ' ')    index_a++;

            while(log_b[index_b] != ' ')    index_b++;


            string real_a = log_a.substr(index_a+1);
            string real_b = log_b.substr(index_b+1);
            if(real_a == real_b){
                return log_a.substr(0, index_a) < log_b.substr(0, index_b);
            }
            else{
                return real_a < real_b;
            }
        });

        chara_log.insert(chara_log.end(), num_log.begin(), num_log.end());
        return chara_log;
    }
};
```

官方题解代码和我的实现思路基本一致，但细节处理上有一些差别：没有对两种类型分别讨论，在查找首个空格时使用了 ``find_first_of`` 函数，当两个字符串日志内容相同时需要对 tag 进行比较时，不需要专门截取 tag 直接将两个字符串进行比较即可。

```cpp
class Solution {
public:
    vector<string> reorderLogFiles(vector<string>& logs) {
        stable_sort(logs.begin(), logs.end(), [&](const string & log1, const string & log2) {
            int pos1 = log1.find_first_of(" ");
            int pos2 = log2.find_first_of(" ");
            bool isDigit1 = isdigit(log1[pos1 + 1]);
            bool isDigit2 = isdigit(log2[pos2 + 1]);
            if (isDigit1 && isDigit2) {
                return false;
            }
            if (!isDigit1 && !isDigit2) {
                string s1 = log1.substr(pos1);
                string s2 = log2.substr(pos2);
                if (s1 != s2) {
                    return s1 < s2;
                }
                return log1 < log2;
            }
            return isDigit1 ? false : true;
        });
        return logs;
    }
};

// 作者：LeetCode-Solution
// 链接：https://leetcode-cn.com/problems/reorder-data-in-log-files/solution/zhong-xin-pai-lie-ri-zhi-wen-jian-by-lee-egtm/
// 来源：力扣（LeetCode）
// 著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
```