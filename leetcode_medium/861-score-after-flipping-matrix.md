## 891. 翻转矩阵后的得分

2020-12-07 15:34:50

### 题目

有一个二维矩阵 ``A`` 其中每个元素的值为 ``0`` 或 ``1`` 。

移动是指选择任一行或列，并转换该行或列中的每一个值：将所有 ``0`` 都更改为 ``1``，将所有 ``1`` 都更改为 ``0``。

在做出任意次数的移动后，将该矩阵的每一行都按照二进制数来解释，矩阵的得分就是这些数字的总和。

返回尽可能高的分数。

**示例：**

```
输入：[[0,0,1,1],[1,0,1,0],[1,1,0,0]]
输出：39
解释：
转换为 [[1,1,1,1],[1,0,0,1],[1,1,1,1]]
0b1111 + 0b1001 + 0b1111 = 15 + 9 + 15 = 39
```

 

**提示：**

- ``1 <= A.length <= 20``
- ``1 <= A[0].length <= 20``
- ``A[i][j]`` 是 ``0`` 或 ``1``



### 思路及代码

首先进行行翻转，使每行第一个元素均为一，之后从第二列进行列翻转，保证每列1的个数大于0。

```cpp
class Solution {
public:
    int getNum(vector<int>& nums){
        int res = 0;
        for(int i = 0; i < nums.size(); i++){
            res = res * 2 + nums[i];
        }
        return res;
    }
    int matrixScore(vector<vector<int>>& A) {
        // 行翻转使每一列的第一个数为1
        for(int i = 0; i < A.size(); i++){
            if(A[i][0] == 0){
                for(int j = 0; j < A[i].size(); j++){
                    A[i][j] = (A[i][j] + 1) % 2;
                }
            }
        }

        // 检查每列保证1的个数大于0
        int aim = (A.size() + 1) / 2;
        for(int j = 1; j < A[0].size(); j++){
            int count = 0;
            for(int i = 0; i < A.size(); i++){
                if(A[i][j]){
                    count++;
                }
            }
            if(count < aim){
                for(int i = 0; i < A.size(); i++){
                    A[i][j] = (A[i][j] + 1) % 2;
                }
            }
        }

        // 计数
        int res = 0;
        for(int i = 0; i < A.size(); i++){
            res += getNum(A[i]);
        }
        return res;
    }
};
```