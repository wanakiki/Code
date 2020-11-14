## 922. 按奇偶排序数组 II

2020年11月14日

### 题目

给定一个非负整数数组 ``A``， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 ``A[i]`` 为奇数时，``i`` 也是奇数；当 ``A[i]`` 为偶
数时， ``i`` 也是偶数。

你可以返回任何满足上述条件的数组作为答案。



**示例：**

```
输入：[4,2,5,7]
输出：[4,5,2,7]
解释：[4,7,2,5]，[2,5,4,7]，[2,7,4,5] 也会被接受。
```



**提示：**


- ``2 <= A.length <= 20000``
- ``A.length % 2 == 0``
- ``0 <= A[i] <= 1000``

### 思路及代码

当所有的偶数都位于偶数位置上时，所有的奇数同样位于奇数位置上。

```cpp
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        // 偶数位于偶数位置意味着奇数位于奇数位置
        int left = 0, right = 0;
        while(right < A.size()){
            if(!(A[right] & 1) && (right & 1)){
                int tmp = A[right];
                A[right] = A[left];
                A[left] = tmp;
                right--;
                left += 2;
            }
            right++;
        }
        return A;
    }
};
```

上面的代码进行了一些不必要的判断，并且有可能重复操作已经在偶数位置上的偶数，可以进一步优化：

```cpp
class Solution {
public:
    vector<int> sortArrayByParityII(vector<int>& A) {
        // 偶数位于偶数位置意味着奇数位于奇数位置
        int even = 0, odd = 1;
        while(even < A.size()){
            if(A[even] & 1){
                // 找到下一个奇数位置
                while(A[odd] & 1){
                    odd += 2;
                }
                swap(A[even], A[odd]);
            }
            even += 2;
        }
        return A;
    }
};
```