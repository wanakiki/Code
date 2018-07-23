## 223. Rectangle Area
##### 2018年7月23日
***
### 题目
Find the total area covered by two rectilinear rectangles in a 2D plane.

Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.

![Rectangle Area](https://leetcode.com/static/images/problemset/rectangle_area.png)

Example:

Input: A = -3, B = 0, C = 3, D = 4, E = 0, F = -1, G = 9, H = 2
Output: 45
Note:

Assume that the total area is never beyond the maximum possible value of int.

### 分析
这道题大学以来见到过很多次，现在已经相当面熟了。

最原始的做法是根据一个矩形的坐标建立一个数组，然后再根据另一个矩形的坐标遍历这个数组，判断是否有交集并计数，最后计算得出总面积。

但实际上可以用另一种做法去解决这个题目，同样先算出来两个矩形的面积，之后再减去中间交集的面积。相交部分的左端点是给出两个矩形左端点的最大值，右端点是给出两个矩形右端点的最小值，同理得到上下坐标。

### 示例代码
C++:
```cpp
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int total_temp = (C - A) * (D - B) + (G - E) * (H - F);
        if (E >= C || F >= D || B >= H || A >= G) return total_temp;
        return total_temp - ((min(G, C) - max(A, E)) * (min(D, H) - max(B, F)));
    }
};
```
最快的方法:
```cpp
static const auto _____ = []()
{
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    return nullptr;
}();
class Solution {
public:
    int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {
        int area1 = (C - A)*(D - B);
        int area2 = (G - E)*(H - F);

        if(C<=E || A>=G || B>=H || D<=F) {
            return area1 + area2;
        }
        else {
            vector <int> h;
            h.push_back(A);
            h.push_back(C);
            h.push_back(E);
            h.push_back(G);

            vector <int> v;
            v.push_back(B);
            v.push_back(D);
            v.push_back(F);
            v.push_back(H);

            sort(h.begin(), h.end());
            sort(v.begin(), v.end());

            int area3 = (h[2] - h[1])*(v[2] - v[1]);
            return area1 + area2 - area3;
        }
    }
};
```
