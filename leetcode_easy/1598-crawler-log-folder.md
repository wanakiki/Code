## 1598. 文件夹操作日志搜集器

2022-09-09 15:06:04

### 题目

每当用户执行变更文件夹操作时，LeetCode 文件系统都会保存一条日志记录。

下面给出对变更操作的说明：


- ``"../"`` ：移动到当前文件夹的父文件夹。如果已经在主文件夹下，则 **继续停留在当前文件夹** 。
- ``"./"`` ：继续停留在当前文件夹**。**
- ``"x/"`` ：移动到名为 ``x`` 的子文件夹中。题目数据 **保证总是存在文件夹 ``x``** 。


给你一个字符串列表 ``logs`` ，其中 ``logs[i]`` 是用户在 ``i<sup>th</sup>`` 步执行的操作。

文件系统启动时位于主文件夹，然后执行 ``logs`` 中的操作。

执行完所有变更文件夹操作后，请你找出 **返回主文件夹所需的最小步数** 。



**示例 1：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_11_1957.png" style="height: 151px; width: 775px;">

```
输入：logs = ["d1/","d2/","../","d21/","./"]
输出：2
解释：执行 "../" 操作变更文件夹 2 次，即可回到主文件夹
```

**示例 2：**

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2020/09/26/sample_22_1957.png" style="height: 270px; width: 600px;">

```
输入：logs = ["d1/","d2/","./","d3/","../","d31/"]
输出：3
```

**示例 3：**

```
输入：logs = ["d1/","../","../","../"]
输出：0
```



**提示：**


- ``1 <= logs.length <= 10<sup>3</sup>``
- ``2 <= logs[i].length <= 10``
- ``logs[i]`` 包含小写英文字母，数字，``'.'`` 和 ``'/'``
- ``logs[i]`` 符合语句中描述的格式
- 文件夹名称由小写英文字母和数字组成



[LeetCode链接](https://leetcode-cn.com/problems/crawler-log-folder/)

### 思路及代码

不需要构建目录树，需要记录当前所在的层数，遇到文件夹名称层数加一，遇到``..``层数减一，注意层数最小值为零。当处理完所有的字符串后返回层数即可。

```cpp
class Solution {
public:
    int minOperations(vector<string>& logs) {
        int cur = 0;
        for(auto log : logs){
            if(log[0] == '.'){
                if(log[1] == '.'){
                    cur--;
                    if(cur < 0) cur = 0;
                }
            }
            else{
                cur++;
            }
        }
        return cur;
    }
};
```