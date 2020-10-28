## 1207. 独一无二的出现次数

2020年10月28日

### 题目
给你一个整数数组 ``arr``，请你帮忙统计数组中每个数的出现次数。

如果每个数的出现次数都是独一无二的，就返回 ``true``；否则返回 ``false``。



**示例 1：**

```
输入：arr = [1,2,2,1,1,3]
输出：true
解释：在该数组中，1 出现了 3 次，2 出现了 2 次，3 只出现了 1 次。没有两个数的出现次数相同。
```

**示例 2：**

```
输入：arr = [1,2]
输出：false
```

**示例 3：**

```
输入：arr = [-3,0,1,-3,1,1,1,-3,10,0]
输出：true
```



**提示：**


- ``1 <= arr.length <= 1000``
- ``-1000 <= arr[i] <= 1000``

### 思路及代码

对原数组进行排序，之后遍历数组，用哈希表存放数字出现的次数。

```cpp
class Solution {
public:
    bool uniqueOccurrences(vector<int>& arr) {
        sort(arr.begin(), arr.end());
        unordered_map<int, int> hash;
        int count = 0;
        for(int i = 0; i < arr.size(); i++){
            count++;
            if(i == arr.size() -1 || arr[i] != arr[i+1]){       // 最后一个元素不需要特殊的判断，一定是计数终止位置
                // 判断是否能找到
                if(hash.find(count) == hash.end()){
                    hash[count] = arr[i];
                    count = 0;
                }
                else{
                    return false;
                }
            }
        }
        return true;
    }
};
```