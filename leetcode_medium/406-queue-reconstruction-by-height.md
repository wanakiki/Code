## 406. 根据身高重建队列

2020-11-16 12:40:19

### 题目

假设有打乱顺序的一群人站成一个队列。 每个人由一个整数对``(h, k)``表示，其中``h``是这个人的身高，``k``是排在这个人前面且身高大于或等于``h``的人数。 编写一个算法来重建这个队列。

**注意：**

总人数少于1100人。

**示例**

```

输入:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

输出:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]
```


### 思路及代码

首先按照h升序，k升序对原数组排序，这时便能从身高较低的人开始逐个放入队列，不难发现放入队列的位置是在上个高度的人被放置之后，第k+1个空白位置处。照此思路便可实现代码。

但是官方题解将排序方式更换为h升序k降序，先放入的元素不会放置到后放置元素的前面，就不需要进行额外的保存。

```cpp
class Solution {
public:
    vector<vector<int>> reconstructQueue(vector<vector<int>>& people) {
        sort(people.begin(), people.end(), [&](const vector<int>& a, const vector<int>& b){
            return a[0] < b[0] || (a[0] == b[0] && a[1] > b[1]);
        });
        
        vector<vector<int>> res(people.size());
        for(int i = 0; i < people.size(); i++){
            int pos = people[i][1];
            for(int j = 0; j < people.size(); j++){
                if(res[j].empty()){
                    if(!pos){
                        res[j] = people[i];
                        break;
                    }
                    pos--;
                }
            }
        }
        return res;
    }
};
```