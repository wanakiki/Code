## 120. Triangle
##### 2018-04-30 22:54:42
##### 三角形查找最小路径（动态规划）
*****
## 题目
Given a triangle, find the minimum path sum from top to bottom. Each step you may move to adjacent numbers on the row below.

For example, given the following triangle
```
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
```
The minimum path sum from top to bottom is 11 (i.e., 2 + 3 + 5 + 1 = 11).

Note:

Bonus point if you are able to do this using only O(n) extra space, where n is the total number of rows in the triangle.

给定一个三角形数组，从上到下找到最小的路径和，每一步只可以移动到下一行的相邻数字。
## 分析
注意到只能移动到下一行的相邻数字，所以我们可以采取动态规划的方法。从下到上处理非常简单，不做过多解释。具体请看示例代码↓↓↓
## 示例代码
```cpp
class Solution {
public:
    int minimumTotal(vector<vector<int>>& triangle) {
        vector<int> res=triangle.back();    //将最后一行数据复制一份用于动态规划
        for(int i=triangle.size()-2;i>=0;i--){
            for(int j=0;j<=i;j++)
                res[j]=triangle[i][j]+min(res[j],res[j+1]);
                //应该注意这里需要从零开始处理，
                //如果从最大位置开始处理则前面的数字判断的就有可能是已经处理过的数据
        }
        return res[0];
    }
};
```
