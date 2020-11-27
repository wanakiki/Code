## 454. 四数相加 II

2020-11-27 21:16:14

### 题目

给定四个包含整数的数组列表 A , B , C , D ,计算有多少个元组 ``(i, j, k, l)`` ，使得 ``A[i] + B[j] + C[k] + D[l] = 0``。

为了使问题简单化，所有的 A, B, C, D 具有相同的长度 N，且 0 &le; N &le; 500 。所有整数的范围在 -2<sup>28</sup> 到 2<sup>28</sup> - 1 之间，最终结果不会超过 2<sup>31</sup> - 1 。

**例如:**

```

输入:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

输出:
2

解释:
两个元组如下:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
```


### 思路及代码

针对于这种多数之和类型的题目，如果使用搜索的做法，遍历所有可能性所需要的复杂度为O(n^m)，其中m为所使用数的个数，为了降低算法的复杂度，可以将其进行分组。以本题中的4组数据为例，分组情况有(2, 2)，(1, 3)两种，前者的复杂度为O(n^2)，后者复杂度为O(n^3)，因此分组的目的是使分组之后，每组的最大个数尽可能小。

```cpp
class Solution {
public:
    int fourSumCount(vector<int>& A, vector<int>& B, vector<int>& C, vector<int>& D) {
        unordered_map<int, int> hash1;
        for(int i = 0; i < A.size(); i++){
            for(int j = 0; j < B.size(); j++){
                int cur = A[i] + B[j];
                if(hash1.find(cur) == hash1.end()){
                    hash1[cur] = 1;
                }
                else{
                    hash1[cur]++;
                }
            }
        }

        int res = 0;
        for(int i = 0; i < C.size(); i++){
            for(int j = 0; j < D.size(); j++){
                int cur = C[i] + D[j];
                cur = -cur;
                if(hash1.find(cur) != hash1.end()){
                    res += hash1[cur];
                }
            }
        }
        return res;
    }
};
```