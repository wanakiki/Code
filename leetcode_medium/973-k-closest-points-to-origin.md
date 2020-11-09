## 973. 最接近原点的 K 个点

2020年11月9日

### 题目

我们有一个由平面上的点组成的列表 ``points``。需要从中找出 ``K`` 个距离原点 ``(0, 0)`` 最近的点。

（这里，平面上两点之间的距离是欧几里德距离。）

你可以按任何顺序返回答案。除了点坐标的顺序之外，答案确保是唯一的。



**示例 1：**

```
输入：points = [[1,3],[-2,2]], K = 1
输出：[[-2,2]]
解释：
(1, 3) 和原点之间的距离为 sqrt(10)，
(-2, 2) 和原点之间的距离为 sqrt(8)，
由于 sqrt(8) < sqrt(10)，(-2, 2) 离原点更近。
我们只需要距离原点最近的 K = 1 个点，所以答案就是 [[-2,2]]。
```

**示例 2：**

```
输入：points = [[3,3],[5,-1],[-2,4]], K = 2
输出：[[3,3],[-2,4]]
（答案 [[-2,4],[3,3]] 也会被接受。）
```



**提示：**


- ``1 <= K <= points.length <= 10000``
- ``-10000 < points[i][0] < 10000``
- ``-10000 < points[i][1] < 10000``
- 
### 思路及代码

计算每个点距离原点的欧几里得距离，之后自定义排序函数，排序之后取前K个数。


```cpp
class Solution {
public:
    static bool cmp(const pair<int, int>& a, const pair<int, int>& b){
        return a.first < b.first;
    }
    vector<vector<int>> kClosest(vector<vector<int>>& points, int K) {
        vector<pair<int, int>> distance;
        for(int i = 0; i < points.size(); i++){
            int tmp = points[i][0] * points[i][0] + points[i][1] * points[i][1];
            distance.push_back(make_pair(tmp, i));
        }
        sort(distance.begin(), distance.end(), cmp);

        vector<vector<int>> res;
        for(int i = 0; i < K; i++){
            res.push_back(points[distance[i].second]);
        }
        return res;
    }
};
```

上面这段代码中创建distance数组不是必须的，可以直接把求解距离写在排序函数里，但是这样会增加额外的计算量。

上面算法的复杂度为O(nlogn)，当考虑到数组中的点数过大时可以维护长度为K的堆，将算法的复杂度降低到O(nlogK)，但由于对数函数的特点，带来的提升可能不是很明显。C++中优先级队列便是大根堆。