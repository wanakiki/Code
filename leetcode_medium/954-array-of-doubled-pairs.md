## 954. 二倍数对数组

2022-04-01 16:37:45 

### 题目

给定一个长度为偶数的整数数组 ``arr``，只有对 ``arr`` 进行重组后可以满足 “对于每个 ``0 <= i < len(arr) / 2``，都有 ``arr[2 * i + 1] = 2 * arr[2 * i]``” 时，返回 ``true``；否则，返回 ``false``。



**示例 1：**

```
输入：arr = [3,1,3,6]
输出：false
```

**示例 2：**

```
输入：arr = [2,1,2,6]
输出：false
```

**示例 3：**

```
输入：arr = [4,-2,2,-4]
输出：true
解释：可以用 [-2,-4] 和 [2,4] 这两组组成 [-2,-4,2,4] 或是 [2,4,-2,-4]
```



**提示：**


- ``0 <= arr.length <= 3 * 10<sup>4</sup>``
- ``arr.length`` 是偶数
- ``-10<sup>5</sup> <= arr[i] <= 10<sup>5</sup>``



[LeetCode链接](https://leetcode-cn.com/problems/array-of-doubled-pairs/)

### 思路及代码

题目的要求是对所有元素都找到与其配对的元素，基本思路是用哈希表统计元素次数，然后查找配对情况。排序之后再进行处理会比较简单，需要注意数值为零的特殊情况。虽然基本思路比较简单，但是需要处理的细节偏多，需要好好考虑。

```cpp
class Solution {
public:
    bool canReorderDoubled(vector<int>& arr) {
        // 相邻两个数字满足二倍关系
        // 且不存在交叉引用 2 4 8 2 必然不成立 每个数字都应配对
        sort(arr.begin(), arr.end());
        unordered_map<int, int> hash;
        for(auto n : arr){
            hash[n]++;
        }

        int count = 0;
        for(auto n : arr){
            if(hash.find(n) == hash.end())  continue;
            // 如果是偶数 且不为零
            if(n % 2 == 0 && n != 0){
                if(hash.find(n / 2) != hash.end()){
                    count++;

                    // 删除已经使用的元素对
                    if(hash[n/2] == 1){
                        hash.erase(n/2);
                    }
                    else{
                        hash[n/2]--;
                    }

                    if(hash[n] == 1){
                        hash.erase(n);
                    }
                    else{
                        hash[n]--;
                    }
                }
            }
        }

        // 零只能和零匹配
        if(hash.find(0) != hash.end()){
            count += hash[0] / 2;
        }
        if(count == arr.size() / 2) return true;
        else    return false;
    }
};
```