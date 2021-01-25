## 999. 由斜杠划分区域

2021-01-25 19:04:25

### 题目

在由 1 x 1 方格组成的 N x N 网格 ``grid`` 中，每个 1 x 1 方块由 ``/``、``\`` 或空格构成。这些字符会将方块划分为一些共边的区域。

（请注意，反斜杠字符是转义的，因此 ``\`` 用 ``"\\"`` 表示。）。

返回区域的数目。

 
**示例 1：**

```
输入：
[
  " /",
  "/ "
]
输出：2
解释：2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/1.png">
```

**示例 2：**

```
输入：
[
  " /",
  "  "
]
输出：1
解释：2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/2.png">
```

**示例 3：**

```
输入：
[
  "\\/",
  "/\\"
]
输出：4
解释：（回想一下，因为 \ 字符是转义的，所以 "\\/" 表示 \/，而 "/\\" 表示 /\。）
2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/3.png">
```

**示例 4：**

```
输入：
[
  "/\\",
  "\\/"
]
输出：5
解释：（回想一下，因为 \ 字符是转义的，所以 "/\\" 表示 /\，而 "\\/" 表示 \/。）
2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/4.png">
```

**示例 5：**

```
输入：
[
  "//",
  "/ "
]
输出：3
解释：2x2 网格如下：
<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2018/12/15/5.png">
```

 

**提示：**


- ``1 <= grid.length == grid[0].length <= 30``
- ``grid[i][j]`` 是 ``'/'``、``'\'``、或 ``' '``。



### 思路及代码

并查集老套路，可以用标准模板来做这个题。比较难想到的一点是如何把单个网格代表的信息表达出来，这里借鉴了官方题解的做法，将一个格子分为上下左右四个部分，再将二维的网格转化为一维和并查集匹配，感觉对了解并查集的人来说是一个比较好的题目，避免死板地应用。

```cpp
class UnionSet {
public:
    vector<int> parent;
    int count;
    UnionSet(int n){
        for(int i = 0; i < n; i++){
            parent.push_back(i);
        }
        count = n;
    }

    void unionx(int x, int y){
        int a = findx(x);
        int b = findx(y);
        if(a != b){
            parent[b] = a;
            count--;
        }
    }

    int findx(int x){
        if(parent[x] != x){
            parent[x] = findx(parent[x]);
        }
        return parent[x];
    }
};
class Solution {
public:
    int regionsBySlashes(vector<string>& grid) {
        // 每个网格被划分为上下左右四个部分 从上方开始顺时针编号
        int len = grid.size();
        int size = len * len * 4;
        int row = len * 4;  // 每行个数
        UnionSet us(size);
        for(int i = 0; i < len; i++){
            for(int j = 0; j < len; j++){
                int cur = row * i + j * 4;
                char c = grid[i][j];
                if(c == ' '){
                    us.unionx(cur, cur + 1);
                    us.unionx(cur + 1, cur + 2);
                    us.unionx(cur + 2, cur + 3);
                }
                else if(c == '/'){
                    us.unionx(cur, cur + 3);
                    us.unionx(cur + 1, cur + 2);
                }
                else{
                    us.unionx(cur, cur + 1);
                    us.unionx(cur + 2, cur + 3);
                }

                // 向下合并
                if(i + 1 < len){
                    us.unionx(cur + 2, cur + row);
                }
                // 向右合并
                if(j + 1 < len){
                    us.unionx(cur + 1, cur + 7);
                }
            }
        }
        return us.count;
    }
};
```

另外，还有一种做法是将每个格子转化为3*3的数组，用0代表空白，1代表斜线，那么整个问题就变成了与求岛屿的数量相近的题目。
