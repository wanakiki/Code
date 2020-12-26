## 85. 最大矩形    

2020-12-26 20:51:39

### 题目

给定一个仅包含 ``0`` 和 ``1`` 、大小为 ``rows x cols`` 的二维二进制矩阵，找出只包含 ``1`` 的最大矩形，并返回其面积。      

 

**示例 1：**
<img alt="" src="https://assets.leetcode.com/uploads/2020/09/14/maximal.jpg" style="width: 402px; height: 322px;" />      
```

输入：matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
输出：6
解释：最大矩形如上图所示。
```

**示例 2：**

```

输入：matrix = []
输出：0
```

**示例 3：**

```

输入：matrix = [["0"]]
输出：0
```

**示例 4：**

```

输入：matrix = [["1"]]
输出：1
```

**示例 5：**

```

输入：matrix = [["0","0"]]
输出：0
```

 

**提示：**


- ``rows == matrix.length``
- ``cols == matrix[0].length``
- ``0 <= row, cols <= 200``
- ``matrix[i][j]`` 为 ``'0'`` 或 ``'1'``



### 思路及代码

先按照横向或者纵向计算最大的累加和，然后再用84题的做法计算每一行能够得到的最大值。

```cpp
class Solution {
public:
    int helper(vector<int>& nums){
        stack<int> stk;
        int res = 0;
        vector<int> left_edge(nums.size(), -1);
        for(int i = 0; i < nums.size(); i++){
            while(!stk.empty() && nums[stk.top()] >= nums[i]){
                int cur = stk.top();
                stk.pop();
                int cur_len = nums[cur] * (i - left_edge[cur] - 1);
                res = max(res, cur_len);
            }

            if(stk.empty()){
                left_edge[i] = -1;
            }
            else{
                left_edge[i] = stk.top();
            }
            stk.push(i);
        }

        // 清除栈内剩余元素
        int len = nums.size();
        while(!stk.empty()){
            int cur = stk.top();
            stk.pop();
            int cur_len = nums[cur] * (len - left_edge[cur] - 1);
            res = max(res, cur_len);
        }
        return res;
    }
    int maximalRectangle(vector<vector<char>>& matrix) {
        int res = 0;
        if(matrix.size() == 0 || matrix[0].size() == 0){
            return res;
        }

        vector<vector<int>> nums(matrix.size(), vector<int>(matrix[0].size(), 0));

        // 获取纵向累加和
        for(int j = 0; j < nums[0].size(); j++){
            for(int i = 0; i < nums.size(); i++){
                int cur = matrix[i][j] - '0';
                if(i == 0 || cur == 0){
                    nums[i][j] = cur;
                }
                else{
                    nums[i][j] = nums[i-1][j] + 1;
                }
            }
        }

        // 计算每行最大值
        for(int i = 0; i < nums.size(); i++){
            res = max(res, helper(nums[i]));
        }
        return res;
    }
};
```