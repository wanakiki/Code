# 463. Island Perimeter

2018年9月12日

## 题目

You are given a map in form of a two-dimensional integer grid where 1 represents land and 0 represents water. Grid cells are connected horizontally/vertically (not diagonally). The grid is completely surrounded by water, and there is exactly one island (i.e., one or more connected land cells). The island doesn't have "lakes" (water inside that isn't connected to the water around the island). One cell is a square with side length 1. The grid is rectangular, width and height don't exceed 100. Determine the perimeter of the island.

Example:

```no
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

Answer: 16
Explanation: The perimeter is the 16 yellow stripes in the image below:
![tupian](https://leetcode.com/static/images/problemset/island.png)
```

## 分析

给定一个正方形的二维数组，1代表陆地，0代表水，确保陆地紧密相连并且不含有内陆湖，设一块陆地的边长为1求问陆地的周长。

相对简单的计数题，我的做法是设置一个变量res用于计算总面积，遇到一块陆地先加上四条边，之后再判断这块陆地的左边和上边是否有别的陆地，如果有的话各减去两条边，遍历结束之后可以得到最终的周长。

## 示例代码

C++

```cpp
class Solution {
public:
    int islandPerimeter(vector<vector<int>>& grid) {
        int res = 0;
        for(int i = 0; i < grid.size(); i++){
            for(int j = 0; j < grid[i].size(); j++){
                if(grid[i][j] == 1)
                    res += 4;
                else
                    continue;
                if(i != 0 && grid[i - 1][j] == 1)
                    res -= 2;
                if(j != 0 && grid[i][j - 1] == 1)
                    res -= 2;
            }
        }
        return res;
    }
};
```