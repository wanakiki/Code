## 1710. 卡车上的最大单元数

2022-11-15 10:01:52

### 题目

请你将一些箱子装在 **一辆卡车** 上。给你一个二维数组 ``boxTypes`` ，其中 ``boxTypes[i] = [numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub>]`` ：


- ``numberOfBoxes<sub>i</sub>`` 是类型 ``i`` 的箱子的数量。
- ``numberOfUnitsPerBox<sub>i</sub>``<sub> </sub>是类型 ``i`` 每个箱子可以装载的单元数量。


整数 ``truckSize`` 表示卡车上可以装载 **箱子** 的 **最大数量** 。只要箱子数量不超过 ``truckSize`` ，你就可以选择任意箱子装到卡车上。

返回卡车可以装载 **单元** 的 **最大** 总数。

 

**示例 1：**

```
输入：boxTypes = [[1,3],[2,2],[3,1]], truckSize = 4
输出：8
解释：箱子的情况如下：
- 1 个第一类的箱子，里面含 3 个单元。
- 2 个第二类的箱子，每个里面含 2 个单元。
- 3 个第三类的箱子，每个里面含 1 个单元。
可以选择第一类和第二类的所有箱子，以及第三类的一个箱子。
单元总数 = (1 * 3) + (2 * 2) + (1 * 1) = 8
```

**示例 2：**

```
输入：boxTypes = [[5,10],[2,5],[4,7],[3,9]], truckSize = 10
输出：91
```

 

**提示：**


- ``1 <= boxTypes.length <= 1000``
- ``1 <= numberOfBoxes<sub>i</sub>, numberOfUnitsPerBox<sub>i</sub> <= 1000``
- ``1 <= truckSize <= 10<sup>6</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/maximum-units-on-a-truck/)

### 思路及代码

相当于每个物品的体积都是 1 的背包问题，贪心。

```cpp
class Solution {
public:
    int maximumUnits(vector<vector<int>>& boxTypes, int truckSize) {
        sort(boxTypes.begin(), boxTypes.end(), [&](const vector<int>& a, const vector<int>& b){
            return a[1] > b[1];
        });

        int res = 0;
        for(int i = 0; i < boxTypes.size(); i++){
            if(boxTypes[i][0] >= truckSize){
                res += truckSize * boxTypes[i][1];
                truckSize = 0;
                break;
            }
            else{
                res += boxTypes[i][0] * boxTypes[i][1];
                truckSize -= boxTypes[i][0];
            }
        }
        return res;
    }
};
```