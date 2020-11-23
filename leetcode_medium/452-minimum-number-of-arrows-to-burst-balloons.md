## 452. 用最少数量的箭引爆气球

2020-11-23 17:34:48

### 题目

在二维空间中有许多球形的气球。对于每个气球，提供的输入是水平方向上，气球直径的开始和结束坐标。由于它 
是水平的，所以纵坐标并不重要，因此只要知道开始和结束的横坐标就足够了。开始坐标总是小于结束坐标。     

一支弓箭可以沿着 x 轴从不同点完全垂直地射出。在坐标 x 处射出一支箭，若有一个气球的直径的开始和结束坐 
标为 ``x``<sub>``start``，</sub>``x``<sub>``end``，</sub> 且满足  ``x<sub>start</sub> ≤ x ≤ x``<sub>``end``，</sub>则该气球会被引爆<sub>。</sub>可以射出的弓箭的数量没有限制。 弓箭一旦被射出之后，可以无 
限地前进。我们想找到使得所有气球全部被引爆，所需的弓箭的最小数量。

给你一个数组 ``points`` ，其中 points [i] = [x<sub>start</sub>,x<sub>end</sub>] ，返回引爆所有气 
球所必须射出的最小弓箭数。
 

**示例 1：**

```

输入：points = [[10,16],[2,8],[1,6],[7,12]]
输出：2
解释：对于该样例，x = 6 可以射爆 [2,8],[1,6] 两个气球，以及 x = 11 射爆另外两个气球
```

**示例 2：**

```

输入：points = [[1,2],[3,4],[5,6],[7,8]]
输出：4
```

**示例 3：**

```

输入：points = [[1,2],[2,3],[3,4],[4,5]]
输出：2
```

**示例 4：**

```

输入：points = [[1,2]]
输出：1
```

**示例 5：**

```

输入：points = [[2,3],[2,3]]
输出：1
```

 

**提示：**


- 0 <= points.length <= 10<sup>4</sup>
- points[i].length == 2
- -2<sup>31</sup> <= x<sub>start</sub> < x<sub>end</sub> <= 2<sup>31</sup> - 1



### 思路及代码


排序后贪心，按照先左端点升序后右端点升序的规则对原数组进行排序，之后遍历排序后的数组。为了使箭能够贯穿最多的气球，就要求射箭的位置尽可能在重合气球集合中某个气球的右侧，可以用贪心的方法寻找。

```cpp
class Solution {
public:
    int findMinArrowShots(vector<vector<int>>& points) {
        sort(points.begin(), points.end(), [&](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0] || ((a[0] == b[0] && a[1] < b[1]));
        });
        int res = 0;
        int cur = 0;
        bool flag = false;
        for(int i = 0; i < points.size(); i++){
            if(!flag){
                cur = points[i][1];
                flag = true;
            }
            else{
                if(points[i][0] <= cur){
                    cur = min(cur, points[i][1]);
                }
                else{
                    res += 1;
                    cur = points[i][1];
                }
            }
        }
        if(flag){
            res += 1;
        }
        return res;
    }
};
```