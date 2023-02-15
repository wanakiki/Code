## 1210. 穿过迷宫的最少移动次数

2023-02-05 21:16:58

### 题目

你还记得那条风靡全球的贪吃蛇吗？

我们在一个 ``n*n`` 的网格上构建了新的迷宫地图，蛇的长度为 2，也就是说它会占去两个单元格。蛇会从左上角（``(0, 0)`` 和 ``(0, 1)``）开始移动。我们用 ``0`` 表示空单元格，用 1 表示障碍物。蛇需要移动到迷宫的右下角（``(n-1, n-2)`` 和 ``(n-1, n-1)``）。

每次移动，蛇可以这样走：


- 如果没有障碍，则向右移动一个单元格。并仍然保持身体的水平／竖直状态。
- 如果没有障碍，则向下移动一个单元格。并仍然保持身体的水平／竖直状态。
- 如果它处于水平状态并且其下面的两个单元都是空的，就顺时针旋转 90 度。蛇从（``(r, c)``、``(r, c+1)``）移动到 （``(r, c)``、``(r+1, c)``）。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image-2.png" style="height: 134px; width: 300px;">

- 如果它处于竖直状态并且其右面的两个单元都是空的，就逆时针旋转 90 度。蛇从（``(r, c)``、``(r+1, c)``）移动到（``(r, c)``、``(r, c+1)``）。

<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image-1.png" style="height: 121px; width: 300px;">


返回蛇抵达目的地所需的最少移动次数。

如果无法到达目的地，请返回 ``-1``。

 

**示例 1：**

**<img alt="" src="https://assets.leetcode-cn.com/aliyun-lc-upload/uploads/2019/09/28/image.png" style="height: 439px; width: 400px;">**

```
输入：grid = [[0,0,0,0,0,1],
               [1,1,0,0,1,0],
               [0,0,0,0,1,1],
               [0,0,1,0,1,0],
               [0,1,1,0,0,0],
               [0,1,1,0,0,0]]
输出：11
解释：
一种可能的解决方案是 [右, 右, 顺时针旋转, 右, 下, 下, 下, 下, 逆时针旋转, 右, 下]。
```

**示例 2：**

```
输入：grid = [[0,0,1,1,1,1],
               [0,0,0,0,1,1],
               [1,1,0,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,1],
               [1,1,1,0,0,0]]
输出：9
```

 

**提示：**


- ``2 <= n <= 100``
- ``0 <= grid[i][j] <= 1``
- 蛇保证从空单元格开始出发。



[LeetCode链接](https://leetcode-cn.com/problems/minimum-moves-to-reach-target-with-rotations/)

### 思路及代码

ACM 时候遇到过几次的题目，是广度优先搜索的变体，需要将常见广搜问题中的上下左右更改为题目中给出的几种移动方式。由于之前留下的恶习，在写代码的时候使用一个整形压缩了两个点的坐标，并使用了集合来判断某个坐标是否被访问过。代码还有比较多可以优化的地方，时间和空间上都击败了 5% 的提交。

```cpp
class Solution {
public:
int mask = 7;   // 7位二进制标志坐标
    int calculatePos(vector<int> pos){
        return (pos[0] << (mask * 3)) | (pos[1] << (mask * 2)) | (pos[2] << (mask)) | pos[3];
    }
    vector<int> getPos(int pos){
        vector<int> res(4, 0);
        for(int i = 0; i < 4; i++){
            res[i] = (pos >> (mask * ( 3 - i))) & ((1 << mask) - 1);
        }
        return res;
    }
    vector<vector<int>> direction = {{1, 0, 1, 0}, {0,1,0,1}, {0, 0, 1, -1}, {0, 0, -1, 1}};

    int minimumMoves(vector<vector<int>>& grid) {
        unordered_set<int> count_point;
        queue<int> q;
        q.push(calculatePos({0, 0, 0, 1}));
        int cur_len = 0;
        int n = grid.size();
        int target = calculatePos({n-1, n-2, n-1, n-1});

        while(!q.empty()){
            int qsize = q.size();
            while(qsize--){
                int cur_pos = q.front();
                q.pop();

                if(count_point.find(cur_pos) != count_point.end())  continue;
                count_point.insert(cur_pos);

                if(cur_pos == target)   return cur_len;

                
                // 判断移动的可能性
                for(int i = 0; i < 4; i++){
                    vector<int> pos_vec = getPos(cur_pos);
                    // 标志当前水平还是垂直
                    bool vertical = false;
                    if(pos_vec[1] == pos_vec[3])    vertical = true;
                    if(vertical && i == 2) continue;
                    if(!vertical && i == 3) continue;

                    bool flag = false;  // 标志坐标是否合法
                    for(int j = 0; j < 4; j++){
                        pos_vec[j] += direction[i][j];

                        // 检查坐标是否越界
                        if(pos_vec[j] < 0 || pos_vec[j] >= n){
                            flag = true;
                            break;
                        }   
                    }
                    if(flag)    continue;

                    // 检查坐标是否均为0
                    if((grid[pos_vec[0]][pos_vec[1]] == 0 && grid[pos_vec[2]][pos_vec[3]] == 0)){
                        // 增加对旋转的判断
                        if(i > 1){
                            int dia_x = pos_vec[0] + 1;
                            int dia_y = pos_vec[1] + 1;
                            if(grid[dia_x][dia_y] == 0)  q.push(calculatePos(pos_vec));
                        }
                        else{
                            q.push(calculatePos(pos_vec));
                        }
                    }
                }
            }
            cur_len++;
        }
        return -1;
    }
};
```