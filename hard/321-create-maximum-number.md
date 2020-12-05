## 321. 拼接最大数

2020-12-05 16:37:02

### 题目

给定长度分别为 ``m`` 和 ``n`` 的两个数组，其元素由 ``0-9`` 构成，表示两个自然数各位上的数字。现在从这两个数组中选出 ``k (k <= m + n)`` 个数字拼接成一个新的数，要求从同一个数组中取出的数字保持其在原数组中的相对顺序。

求满足该条件的最大数。结果返回一个表示该最大数的长度为 ``k`` 的数组。

**说明: **请尽可能地优化你算法的时间和空间复杂度。

**示例 1:**

```
输入:
nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
输出:
[9, 8, 6, 5, 3]
```

**示例 2:**

```
输入:
nums1 = [6, 7]
nums2 = [6, 0, 4]
k = 5
输出:
[6, 7, 6, 0, 4]
```

**示例 3:**

```
输入:
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
输出:
[9, 8, 9]
```


### 思路及代码

发现能力还是有限，看到这个题目没有一点想法，下面的代码是照着大佬的代码打出来的。基本方法是尝试两个数组取出数目的所有可能，然后将取出的数字进行组合，组合完毕之后比较，保留最大的一个。

``getSub``函数是用单调栈思想取出数组中长度为len的最大子数组，数组长度有限，在用单调栈取数的时候要注意能够丢弃掉的数也是有上限的。

由于按照上面的做法得到的子数组本身不是递减的，所以在进行合并时不能直接采用常见的算法，在遇到元素相同时需要考虑后面的数字，如果一直到某个数组的末尾都相同，则优先取出来长度更长的。

```cpp
class Solution {
public:
    vector<int> maxNumber(vector<int>& nums1, vector<int>& nums2, int k) {
        vector<int> res(k, 0);
        int len1 = nums1.size(), len2 = nums2.size();
        int start = max(0, k - len2), end = min(k, len1);
        for(int i = start; i <= end; i++){
            vector<int> sub_num1(getSub(nums1, i));
            vector<int> sub_num2(getSub(nums2, k-i));
            vector<int> tmp(mergeNum(sub_num1, sub_num2));
            if(cmp(tmp, 0, res, 0)){
                res.swap(tmp);
            }
        }
        return res;
    }
    vector<int> mergeNum(vector<int>& nums1, vector<int>& nums2){
        int x = nums1.size(), y = nums2.size();
        if(x == 0){
            return nums2;
        }
        if(y == 0){
            return nums1;
        }
        int len = x + y;
        vector<int> res(len, 0);
        int index1 = 0, index2 = 0;
        for(int i = 0; i < len; i++){
            if(cmp(nums1, index1, nums2, index2)){
                res[i] = nums1[index1++];
            }
            else{
                res[i] = nums2[index2++];
            }
        }
        return res;
    }
    bool cmp(vector<int>& nums1, int index1, vector<int>& nums2, int index2){
        // 而这长度不等但较长数组的头部由较短数组组成，先选长的
        int len1 = nums1.size();
        int len2 = nums2.size();
        while(index1 < len1 && index2 < len2){
            if(nums1[index1] != nums2[index2]){
                return nums1[index1] > nums2[index2];
            }
            index1++;
            index2++;
            // 二者不等时就要返回，不能像下面一样写
            /*if(nums1[index1++] > nums2[index2++]){
                return true;
            }*/
        }
        return (len1 - index1) > (len2 - index2);
    }
    vector<int> getSub(vector<int>& nums, int len){
        int drop = nums.size() - len;
        vector<int> res(len, 0);
        int index = -1;
        for(int i = 0; i < nums.size(); i++){
            while(index >= 0 && res[index] < nums[i] && drop > 0){
                index--;
                drop--;
            }
            if(index < len - 1){
                res[++index] = nums[i];
            }
            else{
                drop--;
            }
        }
        return res;
    }
};
```