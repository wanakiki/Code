## 1308. 交换字符串中的元素

2021-01-11 16:59:08

### 题目

给你一个字符串 ``s``，以及该字符串中的一些「索引对」数组 ``pairs``，其中 ``pairs[i] = [a, b]`` 表示字符串中的两个索引（编号从 0 开始）。

你可以 **任意多次交换** 在 ``pairs`` 中任意一对索引处的字符。

返回在经过若干次交换后，``s`` 可以变成的按字典序最小的字符串。

 

**示例 1:**

```
输入：s = "dcab", pairs = [[0,3],[1,2]]
输出："bacd"
解释： 
交换 s[0] 和 s[3], s = "bcad"
交换 s[1] 和 s[2], s = "bacd"
```

**示例 2：**

```
输入：s = "dcab", pairs = [[0,3],[1,2],[0,2]]
输出："abcd"
解释：
交换 s[0] 和 s[3], s = "bcad"
交换 s[0] 和 s[2], s = "acbd"
交换 s[1] 和 s[2], s = "abcd"
```

**示例 3：**

```
输入：s = "cba", pairs = [[0,1],[1,2]]
输出："abc"
解释：
交换 s[0] 和 s[1], s = "bca"
交换 s[1] 和 s[2], s = "bac"
交换 s[0] 和 s[1], s = "abc"
```

 

**提示：**


- ``1 <= s.length <= 10^5``
- ``0 <= pairs.length <= 10^5``
- ``0 <= pairs[i][0], pairs[i][1] < s.length``
- ``s`` 中只含有小写英文字母



### 思路及代码

用并查集根据``pairs``将字符串的索引划分为不同的连通块，对每个连通块排序之后，再逐个取出放到对应位置。

```cpp
class Solution {
public:
    int find(vector<int>& nums, int x){
        while(nums[x] != x){
            nums[x] = nums[nums[x]];
            x = nums[x];
        }
        return nums[x];
    }
    string smallestStringWithSwaps(string s, vector<vector<int>>& pairs) {
        int n = s.size();
        vector<int> nums(n);
        for(int i = 0; i < n; i++){
            nums[i] = i;
        }

        // 并查集
        for(int i = 0; i < pairs.size(); i++){
            int x = find(nums, pairs[i][0]);
            int y = find(nums, pairs[i][1]);
            if(x != y){
                nums[y] = x;
            }
        }

        // 遍历数组 找到连通区域顶端的值
        unordered_map<int, priority_queue<char, vector<char>, greater<char>>> my_hash;
        for(int i = 0; i < n; i++){
            int x = find(nums, i);
            my_hash[x].push(s[i]);
        }

        for(int i = 0; i < n; i++){
            int x = find(nums, i);
            s[i] = my_hash[x].top();
            my_hash[x].pop();
        }
        return s;
    }
};
```

在题解区发现了另外一种做法：因为题目已经指出所有的字母均是小写字母，所以可以直接使用长度为26的数组来保存每个连通块的字母，不需要进行排序。