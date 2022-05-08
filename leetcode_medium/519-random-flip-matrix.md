## 519. 随机翻转矩阵

2021-11-27 10:50:16

### 题目

给你一个 ``m x n`` 的二元矩阵 ``matrix`` ，且所有值被初始化为 ``0`` 。请你设计一个算法，随机选取一个满足 ``matrix[i][j] == 0`` 的下标 ``(i, j)`` ，并将它的值变为 ``1`` 。所有满足 ``matrix[i][j] == 0`` 的下标 ``(i, j)`` 被选取的概率应当均等。

尽量最少调用内置的随机函数，并且优化时间和空间复杂度。

实现 ``Solution`` 类：


- ``Solution(int m, int n)`` 使用二元矩阵的大小 ``m`` 和 ``n`` 初始化该对象
- ``int[] flip()`` 返回一个满足 ``matrix[i][j] == 0`` 的随机下标 ``[i, j]`` ，并将其对应格子中的值变为 ``1``
- ``void reset()`` 将矩阵中所有的值重置为 ``0``




**示例：**

```

输入
["Solution", "flip", "flip", "flip", "reset", "flip"]
[[3, 1], [], [], [], [], []]
输出
[null, [1, 0], [2, 0], [0, 0], null, [2, 0]]

解释
Solution solution = new Solution(3, 1);
solution.flip();  // 返回 [1, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
solution.flip();  // 返回 [2, 0]，因为 [1,0] 已经返回过了，此时返回 [2,0] 和 [0,0] 的概率应当相同
solution.flip();  // 返回 [0, 0]，根据前面已经返回过的下标，此时只能返回 [0,0]
solution.reset(); // 所有值都重置为 0 ，并可以再次选择下标返回
solution.flip();  // 返回 [2, 0]，此时返回 [0,0]、[1,0] 和 [2,0] 的概率应当相同
```



**提示：**


- ``1 <= m, n <= 10<sup>4</sup>``
- 每次调用``flip`` 时，矩阵中至少存在一个值为 0 的格子。
- 最多调用 ``1000`` 次 ``flip`` 和 ``reset`` 方法。



[LeetCode链接](https://leetcode-cn.com/problems/random-flip-matrix/)

### 思路及代码

将二维数组使用一维数组保存，之后按照洗牌算法的思路调用随机函数抽取数值。虽然已经减少了调用次数，但是这种做法只是勉强通过了时间要求。

```cpp
class Solution {
public:
    vector<int> nums;
    int real_size = 0;
    int width;

    Solution(int m, int n) {
        nums.resize(m * n);
        for(int i = 0; i < nums.size(); i++){
            nums[i] = i;
        }
        width = n;
        real_size = nums.size();
    }
    
    vector<int> flip() {
        int cur = rand() % (real_size);
        //cout << cur << ' ' << nums[cur] << endl;
        int cur_i = nums[cur] / width;
        int cur_j = nums[cur] % width;

        swap(nums[cur], nums[--real_size]);
        return {cur_i, cur_j};
    }
    
    void reset() {
        real_size = nums.size();
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(m, n);
 * vector<int> param_1 = obj->flip();
 * obj->reset();
 */
 ```