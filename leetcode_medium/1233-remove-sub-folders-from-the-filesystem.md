## 1233. 删除子文件夹

2023-02-08 15:17:50

### 题目

你是一位系统管理员，手里有一份文件夹列表 ``folder``，你的任务是要删除该列表中的所有 **子文件夹**，并以 **任意顺序** 返回剩下的文件夹。

如果文件夹 ``folder[i]`` 位于另一个文件夹 ``folder[j]`` 下，那么 ``folder[i]`` 就是 ``folder[j]`` 的 **子文件夹** 。

文件夹的「路径」是由一个或多个按以下格式串联形成的字符串：<font color="#c7254e"><font face="Menlo, Monaco, Consolas, Courier New, monospace"><span style="font-size:12.6px"><span style="background-color:#f9f2f4">'/'</span></span></font></font> 后跟一个或者多个小写英文字母。


- 例如，``"/leetcode"`` 和 ``"/leetcode/problems"`` 都是有效的路径，而空字符串和 ``"/"`` 不是。


 

**示例 1：**

```
输入：folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
输出：["/a","/c/d","/c/f"]
解释："/a/b" 是 "/a" 的子文件夹，而 "/c/d/e" 是 "/c/d" 的子文件夹。
```

**示例 2：**

```
输入：folder = ["/a","/a/b/c","/a/b/d"]
输出：["/a"]
解释：文件夹 "/a/b/c" 和 "/a/b/d" 都会被删除，因为它们都是 "/a" 的子文件夹。
```

**示例 3：**

```
输入: folder = ["/a/b/c","/a/b/ca","/a/b/d"]
输出: ["/a/b/c","/a/b/ca","/a/b/d"]
```

 

**提示：**


- ``1 <= folder.length <= 4 * 10<sup>4</sup>``
- ``2 <= folder[i].length <= 100``
- ``folder[i]`` 只包含小写字母和 ``'/'``
- ``folder[i]`` 总是以字符 ``'/'`` 起始
- 每个文件夹名都是 **唯一** 的



[LeetCode链接](https://leetcode-cn.com/problems/remove-sub-folders-from-the-filesystem/)

### 思路及代码

字典树的典型应用，可以使用哈希表替代掉数组提升访问效率。

查看官方题解后发现，可以将每个字符串的索引存到节点中，避免后序遍历字典树的时候传递当前的字符串降低效率。

```cpp
class Node{
public:
    bool end_flag;
    vector<Node*> next;

    Node():end_flag(false), next(27, nullptr){};
};
class Solution {
public:
    vector<string> res;
    void helper(Node* cur_node, string cur_path){
        for(int i = 0; i < 26; i++){
            if(cur_node->next[i]){
                helper(cur_node->next[i], cur_path + string(1, 'a' + i));
            }
        }
        if(cur_node->end_flag){
            res.push_back(cur_path);
        }
        else{
            if(cur_node->next[26])
                helper(cur_node->next[26], cur_path + "/");
        }
    }
    vector<string> removeSubfolders(vector<string>& folder) {
        // 添加到字典树
        Node* root = new Node();

        for(auto s : folder){
            Node* cur_node = root;
            for(auto c : s){
                int index = 0;
                if(c == '/'){
                    index = 26;
                }
                else{
                    index = c - 'a';
                }

                if(cur_node->next[index] == nullptr){
                    cur_node->next[index] = new Node();
                }
                cur_node = cur_node->next[index];
            }
            cur_node->end_flag = true;
        }

        // 遍历字典树 返回结果
        helper(root, "");
        return res;
    }
};
```