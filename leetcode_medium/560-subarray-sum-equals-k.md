## 560. 和为K的子数组

2020年5月15日

### 题目

给定一个整数数组和一个整数 **k，**你需要找到该数组中和为 **k **的连续的子数组的个数。

**示例 1 :**

```
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
```

**说明 :**

- 数组的长度为 [1, 20,000]。
- 数组中元素的范围是 [-1000, 1000] ，且整数 **k **的范围是 [-1e7, 1e7]。

### 代码

#### 枚举子区间

这个做法比较容易想到，用两个for循环便能枚举出全部的子区间，然后计算区间和进行判断。计算区间和的过程可以优化，提前计算好数组的累加和，这样在每个子区间都能用O(1)的操作获得对应的总和。

下面是我的代码，数据预处理的复杂度是O(n)，整体复杂度是O(n^2)，但是超出了时间限制。

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0;

        // 计算累加和
        for(int i = 1; i < nums.size(); i++){
            nums[i] += nums[i-1];
        }

        // 反向遍历查找所有可能情况
        for(int i = nums.size()-1; i >= 0; i--){

            // 0~i所有值的情况
            if(nums[i] == k){
                res++;
            }
            for(int j = i-1; j >= 0; j--){
                int tmp = nums[i] - nums[j];
                if(tmp == k){
                    res++;
                }
            }
        }

        return res;
    }
};
```

下面是官方题解的做法，复杂度也是O(n^2)，执行时间在1736ms，感觉也是差一点就要超时。

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int count = 0;
        for (int start = 0; start < nums.size(); ++start) {
            int sum = 0;
            for (int end = start; end >= 0; --end) {
                sum += nums[end];
                if (sum == k) {
                    count++;
                }
            }
        }
        return count;
    }
};
```

#### 哈希表优化

万能的哈希系列，在方法一的基础上进行了改进，确定满足条件的子区间的方式由遍历变为了查找，复杂度为O(n)。

假设有前缀和数组为$pre$，则题目要求是找到所有的$[i,j]$使其满足$pre[j] - pre[i] == k$，对该式进行转换，则有$pre[i] == pre[j] - k$。是用哈希表存储所有$pre$的值，前缀和每累加一位，反向查找是否有$pre[j] - k$的值即可。

```cpp
class Solution {
public:
    int subarraySum(vector<int>& nums, int k) {
        int res = 0, sum = 0;
        unordered_map<int, int> hash;

        hash[0] = 1;    // 前缀零个数时和为0
        for(int i = 0; i < nums.size(); i++){
            sum += nums[i];
            if(hash.find(sum - k) != hash.end()){
                res += hash[sum - k];
            }
            hash[sum]++;
        }
        return res;
    }
};
```