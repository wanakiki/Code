## 200. Number of Islands
##### 2018-05-18 18:32:26
##### 岛屿数量
***
## 题目

Given a 2d grid map of '1's (land) and '0's (water), count the number of islands. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
```
Input:
11110
11010
11000
00000

Output: 1
```
Example 2:
```
Input:
11000
11000
00100
00011

Output: 3
```
## 分析
比较简单的回溯题目，本来以为会运行很慢，发现大部分人和我一个速度。

需要注意一点的是，如果传参为空，就不能连续用两个s.size()

## 示例代码
```cpp
class Solution {
public:
    void change(int i,int j, int len ,int len2,vector<vector<char>>& grid){
        if(grid[i][j]=='1')
            grid[i][j]='0';
        else
            return ;
        if(i>0)
            change(i-1,j,len,len2,grid);
        if(j>0)
            change(i,j-1,len,len2,grid);
        if(i<len-1)
            change(i+1,j,len,len2,grid);
        if(j<len2-1)
            change(i,j+1,len,len2,grid);
    }
    int numIslands(vector<vector<char>>& grid) {
        int sum=0,len=grid.size();
        if(len==0)
            return sum;		//判断完这一步之后才能运行下一步的size()，否则会出现空指针访问
        int len2=grid[0].size();
        for(int i=0;i<len;i++)
            for(int j=0;j<len2;j++){
                if(grid[i][j]=='1'){
                    sum++;
                    change(i,j,len,len2,grid);
                }
            }
        return sum;
    }
};
```
