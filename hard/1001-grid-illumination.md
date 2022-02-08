## 1001. 网格照明

2022-02-08 12:22:10

### 题目

在大小为 ``n x n`` 的网格 ``grid`` 上，每个单元格都有一盏灯，最初灯都处于 **关闭** 状态。

给你一个由灯的位置组成的二维数组 ``lamps`` ，其中 ``lamps[i] = [row<sub>i</sub>, col<sub>i</sub>]`` 表示 **打开** 位于 ``grid[row<sub>i</sub>][col<sub>i</sub>]`` 的灯。即便同一盏灯可能在 ``lamps`` 中多次列出，不会影响这盏灯处于 **打开** 状态 
。

当一盏灯处于打开状态，它将会照亮 **自身所在单元格** 以及同一 **行** 、同一 **列** 和两条 **对角线** 上的 **所有其他单元格** 。

另给你一个二维数组 ``queries`` ，其中 ``queries[j] = [row<sub>j</sub>, col<sub>j</sub>]`` 。对于第 ``j`` 个查询，如果单元
格 ``[row<sub>j</sub>, col<sub>j</sub>]`` 是被照亮的，则查询结果为 ``1`` ，否则为 ``0`` 。在第 ``j`` 次查询之后 [按照查询
的顺序] ，**关闭** 位于单元格 ``grid[row<sub>j</sub>][col<sub>j</sub>]`` 上及相邻 8 个方向上（与单元格 ``grid[row<sub>i</sub>][col<sub>i</sub>]`` 共享角或边）的任何灯。

返回一个整数数组 ``ans`` 作为答案， ``ans[j]`` 应等于第 ``j`` 次查询 ``queries[j]`` 的结果，``1`` 表示照亮，``0`` 表示未 
照亮。



**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_1.jpg" style="height: 209px; width: 750px;" />      
```
输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
输出：[1,0]
解释：最初所有灯都是关闭的。在执行查询之前，打开位于 [0, 0] 和 [4, 4] 的灯。第 0 次查询检查 grid[1][1] 是否被照亮（蓝色方
框）。该单元格被照亮，所以 ans[0] = 1 。然后，关闭红色方框中的所有灯。
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step1.jpg" style="height: 218px; width: 500px;" />  
第 1 次查询检查 grid[1][0] 是否被照亮（蓝色方框）。该单元格没有被照亮，所以 ans[1] = 0 。然后，关闭红色矩形中的所有灯。  
<img alt="" src="https://assets.leetcode.com/uploads/2020/08/19/illu_step2.jpg" style="height: 219px; width: 500px;" />  
```

**示例 2：**

```
输入：n = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,1]]
输出：[1,1]
```

**示例 3：**

```
输入：n = 5, lamps = [[0,0],[0,4]], queries = [[0,4],[0,1],[1,4]]
输出：[1,1,0]
```



**提示：**


- ``1 <= n <= 10<sup>9</sup>``
- ``0 <= lamps.length <= 20000``
- ``0 <= queries.length <= 20000``
- ``lamps[i].length == 2``
- ``0 <= row<sub>i</sub>, col<sub>i</sub> < n``
- ``queries[j].length == 2``
- ``0 <= row<sub>j</sub>, col<sub>j</sub> < n``



[LeetCode链接](https://leetcode-cn.com/problems/grid-illumination/)

### 思路及代码

题目不难，是用哈希表记录每行每列和每条对角线上亮灯的数目，并额外用一个哈希表保存所有灯的位置。两条对角线上的点分别满足横纵坐标差值相等、横纵坐标加和相等的条件，在统计时需要注意每个灯只需要记录一次。

当把所有亮灯数据输入系统后，针对于每个查询的坐标，只要所处行、列、对角线之一存在灯即可向结果数组添加1，否则添加0。完成添加后，对以查询坐标为中心的9个位置进行判断，如果某个位置存在已经打开的灯，则将该位置的灯删除，并将对应行、列、对角线的计数值减一。

在保存已打开灯的位置时，哈希表的键有两个坐标，直接使用pair无法正常查询，需要提供相关哈希函数。考虑到坐标数据不超过整型范围，一个可选方案是将横纵坐标拼合成64位长整形用于查询。

```cpp
class Solution {
public:
    unsigned long long helper(int x, int y){
        return y | ((unsigned long long)x << 32);
    }
    vector<int> gridIllumination(int n, vector<vector<int>>& lamps, vector<vector<int>>& queries) {
        unordered_map<unsigned long long, int> count;
        unordered_map<int, int> row_count;
        unordered_map<int, int> col_count;
        unordered_map<int, int> diagonal_left_count;
        unordered_map<int, int> diagonal_right_count;
        vector<int> res;

        for(int i = 0; i < lamps.size(); i++){
            if(count.find(helper(lamps[i][0], lamps[i][1])) != count.end()) continue;

            count[helper(lamps[i][0], lamps[i][1])] = 1;

            row_count[lamps[i][0]]++;
            col_count[lamps[i][1]]++;
            diagonal_left_count[lamps[i][0] - lamps[i][1]]++;
            diagonal_right_count[lamps[i][1] + lamps[i][0]]++;
        }

        for(int i = 0; i < queries.size(); i++){
            int x = queries[i][0];
            int y = queries[i][1];
            if(row_count.find(x) != row_count.end() || col_count.find(y) != col_count.end() || diagonal_left_count.find(x - y) != diagonal_left_count.end() || diagonal_right_count.find(y + x) != diagonal_right_count.end()){
                res.push_back(1);
            }
            else{
                res.push_back(0);
            }

            for(int j = -1; j < 2; j++){
                for(int k = -1; k < 2; k++){
                    int cur_x = x + j;
                    int cur_y = y + k;

                    if(count.find(helper(cur_x, cur_y)) != count.end()){
                        count.erase(helper(cur_x, cur_y));
                        row_count[cur_x]--;
                        col_count[cur_y]--;
                        diagonal_left_count[cur_x - cur_y]--;
                        diagonal_right_count[cur_y + cur_x]--;

                        if(row_count[cur_x] == 0)   row_count.erase(cur_x);
                        if(col_count[cur_y] == 0)   col_count.erase(cur_y);
                        if(diagonal_left_count[cur_x - cur_y] == 0) diagonal_left_count.erase(cur_x - cur_y);
                        if(diagonal_right_count[cur_y + cur_x] == 0) diagonal_right_count.erase(cur_y + cur_x);
                    }
                }
            }
        }
        return res;
    }
};
```