## 882. 山脉数组的峰顶索引

2021-06-15 17:38:50       

### 题目

符合下列属性的数组 ``arr`` 称为 **山脉数组** ：

- ``arr.length >= 3``
- 存在 ``i``（``0 < i < arr.length - 1``）使得：
  - ``arr[0] < arr[1] < ... arr[i-1] < arr[i] ``
  - ``arr[i] > arr[i+1] > ... > arr[arr.length - 1]``




给你由整数组成的山脉数组 ``arr`` ，返回任何满足 ``arr[0] < arr[1] < ... arr[i - 1] < arr[i] > arr[i + 1] > ... > arr[arr.length - 1]`` 的下标 ``i`` 。

 

**示例 1：**

```
输入：arr = [0,1,0]
输出：1
```

**示例 2：**

```
输入：arr = [0,2,1,0]
输出：1
```

**示例 3：**

```
输入：arr = [0,10,5,2]
输出：1
```

**示例 4：**

```
输入：arr = [3,4,5,1]
输出：2
```

**示例 5：**

```
输入：arr = [24,69,100,99,79,78,67,36,26,19]
输出：2
```

 

**提示：**


- ``3 <= arr.length <= 10<sup>4</sup>``
- ``0 <= arr[i] <= 10<sup>6</sup>``
- 题目数据保证 ``arr`` 是一个山脉数组


 

**进阶：** 很容易想到时间复杂度 ``O(n)`` 的解决方案，你可以设计一个 ``O(log(n))`` 的解决方案吗？


[LeetCode链接](https://leetcode-cn.com/problems/peak-index-in-a-mountain-array/)

### 思路及代码

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // 相邻元素不存在相等情况
        bool last_pair = arr[1] > arr[0];
        for(int i = 2; i < arr.size();i++){
            bool cur_pair = arr[i] > arr[i-1];
            if(cur_pair != last_pair){
                return i - 1;
            }
        }
        return 0;
    }
};
```

```cpp
class Solution {
public:
    int peakIndexInMountainArray(vector<int>& arr) {
        // 相邻元素不存在相等情况 左边上升右边下降
        int left = 1, right = arr.size() - 1;
        while(left < right){
            int mid = left + (right - left) / 2;
            if(arr[mid] > arr[mid - 1]){
                left = mid + 1;
            }
            else{
                right = mid;
            }
        }
        return right - 1;
    }
};
```