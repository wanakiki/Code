## 189. Rotate Array
##### 2018-05-29 21:10:13
##### 旋转数组
***
## 题目

Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
```
Input: [1,2,3,4,5,6,7] and k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
```
Example 2:
```
Input: [-1,-100,3,99] and k = 2
Output: [3,99,-1,-100]
Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
```
Note:

- Try to come up as many solutions as you can, there are at least 3 different ways to solve this problem.
- Could you do it in-place with O(1) extra space?
## 分析
没有分析 做了一个小时没做出来 就这样

## 示例代码
超时代码
```cpp
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int len = nums.size(),i;
        while(k){
            int temp=nums[len-1] ;
            for(i=len-1;i>0;i--){
                nums[i]=nums[i-1];
            }
            nums[i]=temp;
            k--;
        }
        return ;
    }
};
```
替换法，我开始的想法，但是因为解决不了循环最后不想做了...不过今天又想起来了，长度可以被k整除的话，就会出现环，这时候就要注意怎么去解决重合的问题，但是如果不整除就不会有了。
```cpp
 class Solution 
    {
    public:
        void rotate(int nums[], int n, int k) 
        {
            if ((n == 0) || (k <= 0))
                return;
            
            // Make a copy of nums
            vector<int> numsCopy(n);
            for (int i = 0; i < n; i++)
            {
                numsCopy[i] = nums[i];
            }
            
            // Rotate the elements.
            for (int i = 0; i < n; i++)
            {
                nums[(i + k)%n] = numsCopy[i];
            }
        }
    };
```
