## 221. Maximal Square
##### 2018年7月20日
***
### 题目
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example:
```
Input:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0

Output: 4
```
### 分析
要求最大正方形的面积，最一开始的想法是遍历全部，但是会比较麻烦，试着去减少了一些循环，结果代码提交后有很多漏洞。

在这篇[博客](https://www.cnblogs.com/grandyang/p/4550604.html)上看到了四种解法，我觉得直方图的原理是今后要想到的一点。因为数组的元素只有零和一，所以将每列元素相加就可以判断这一列是否全为1。

比较好的做法是动态规划，因为一个点能否构成正方形的右下角和它左侧、上方、斜上方的点有关，推出状态转移方程:
- matrix[i][j]为1：
```
dp[i][j] = min(dp[i-1][j-1], min(dp[i-1][j], dp[i][j-1])) + 1
```
- matrix[i][j]为0：
```
dp[i][j] = 0
```

### 示例代码
C++：
```cpp
class Solution {
public:
    int maximalSquare(vector<vector<char>>& matrix) {
        int len1 = matrix.size();
        if(!len1)
            return 0;
        int len2 = matrix[0].size();
        int dp[len1 + 2][len2 + 2];
        for(int i =0; i < len1 + 2; i++)
            for(int j = 0; j < len2 + 2; j++)
                dp[i][j] = 0;
        int x = 1, y = 1;
        int max_size = 0;
        for(int i = 0; i < len1; i++){
            x = i + 1;
            for(int j = 0; j < len2; j++){
                y = j + 1;
                if(matrix[i][j] == '0')
                    dp[x][y] = 0;
                else{
                    dp[x][y] = min(dp[x-1][y-1], dp[x-1][y]);
                    dp[x][y] = min(dp[x][y-1], dp[x][y]) + 1;
                    max_size = max(dp[x][y], max_size);
                }
                //y++;
            }
            //x++;
        }
        return max_size*max_size;
    }
};
```
写的比较麻烦
