## 1337. 矩阵中战斗力最弱的 K 行

2021-08-01 19:56:31

### 题目

给你一个大小为 ``m * n`` 的矩阵 ``mat``，矩阵由若干军人和平民组成，分别用 1 和 0 表示。

请你返回矩阵中战斗力最弱的 ``k`` 行的索引，按从最弱到最强排序。

如果第<em>**i**</em> 行的军人数量少于第<em>**j**</em> 行，或者两行军人数量相同但<em>**i**</em> 小于<em>**j**</em>，那么我们认为第<em>**i**</em>行的战斗力比第<em>**j**</em>行弱。

军人 **总是** 排在一行中的靠前位置，也就是说 1 总是出现在 0 之前。

 

**示例 1：**

```

输入：mat =
[[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]],
k = 3
输出：[2,0,3]
解释：
每行中的军人数目：
行 0 -> 2
行 1 -> 4
行 2 -> 1
行 3 -> 2
行 4 -> 5
从最弱到最强对这些行排序后得到 [2,0,3,1,4]
```

**示例 2：**

```

输入：mat =
[[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]],
k = 2
输出：[0,2]
解释：
每行中的军人数目：
行 0 -> 1
行 1 -> 4
行 2 -> 1
行 3 -> 1
从最弱到最强对这些行排序后得到 [0,2,3,1]
```

 

**提示：**


- ``m == mat.length``
- ``n == mat[i].length``
- ``2 <= n, m <= 100``
- ``1 <= k <= m``
- ``matrix[i][j]`` 不是 0 就是 1



[LeetCode链接](https://leetcode-cn.com/problems/the-k-weakest-rows-in-a-matrix/)

### 思路及代码

小顶堆，但是不确定下滤的时候对强度相等的情况作何判断，代码写的也不够简练。

```cpp
class TopK {
public:
    vector<int> data;
    unordered_map<int, int> hash;   // 存储索引与军人数量的关系
    int size;
    int len;

    TopK(int n){
        data.resize(n+1);
        size = 1;
        len = n;
    }

    void add_data(int index, int num){
        hash[index] = num;

        int cur = size;     // 新值索引
        data[size++] = index;       // 保证数组长度足够 不需要做额外判断

        // 上滤
        while(cur > 1){
            int parent = cur / 2;
            int next = cur;
            // 小顶堆
            if(hash[data[cur]] < hash[data[parent]]){
                int tmp = data[parent];
                data[parent] = data[cur];
                data[cur] = tmp;
                next = parent;
            }
            if(next == cur){
                break;
            }
            else{
                cur = next;
            }
        }
    }

    // 判断是否需要交换
    bool judge_val(int parent, int child){
        if(parent >= size || child >= size) return false;

        if(hash[data[parent]] > hash[data[child]] || (hash[data[parent]] == hash[data[child]] && data[parent] > data[child])){
            return true;
        }
        return false;
    }
    int pop_top(){
        int res = data[1];
        data[1] = data[--size];

        // 下滤
        int cur = 1;
        while(cur < size){
            int child_1 = cur * 2;
            int child_2 = child_1 + 1;
            int min_child = cur;
            int next = cur;
            
            // 和两个子节点中较小的一个比较
            if(child_1 < size){
                min_child = child_1;
            }
            if(child_2 < size){
                if(judge_val(child_1, child_2)){
                    min_child = child_2;
                }
            }
            if(min_child == cur){
                break;
            }
            else{
                if(judge_val(cur, min_child)){
                    int tmp = data[cur];
                    data[cur] = data[min_child];
                    data[min_child] = tmp;
                    next = min_child;
                }
            }

            // 判断是否可以继续下滤
            if(cur == next){
                break;
            }
            else{
                cur = next;
            }
        }

        return res;
    }
    void show_val(){
        for(int i = 1; i < size; i++){
            cout << data[i] << ' ' << hash[data[i]] << endl;
        }
        cout << "====" << endl;
    }
    vector<int> get_res(int k){
        vector<int> res;
        // show_val();
        for(int i = 0; i < k; i++){
            res.push_back(pop_top());
        }
        return res;
    }
};
class Solution {
public:
    vector<int> kWeakestRows(vector<vector<int>>& mat, int k) {
        TopK tk(mat.size());
        for(int i = 0; i < mat.size(); i++){
            int count = 0;
            for(int j = 0; j < mat[i].size(); j++){
                if(mat[i][j] == 1){
                    count++;
                }
                else{
                    break;
                }
            }
            tk.add_data(i, count);
        }
        return tk.get_res(k);
    }
};
```