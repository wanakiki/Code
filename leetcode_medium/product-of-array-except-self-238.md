## 238. Product of Array Except Self
###### 2018年7月24日
***
### 题目
Given an array nums of n integers where n > 1,  return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:
```
Input:  [1,2,3,4]
Output: [24,12,8,6]
```
Note: Please solve it **without division** and in O(n).

Follow up:

Could you solve it with constant space complexity? (The output array does not count as extra space for the purpose of space complexity analysis.)

### 分析
要求不用除法得到一个数组，新数组的值是原数组中除该位置以外所有元素的乘积。

不用除法，很明显，只要新数组的元素不乘对应原数组的对应值就可以了。如果数学经验比较多的话，比较容易就会发现对于一个数字，只要知道前面所有数字的乘积和后面所有数字的乘积，二者相乘就是我们要的结果。

所以眼下应该创建出两个数组，分别包含所求元素之前所有元素的乘积和之后所有元素的乘积。（可能这种创造方式以后会用得到，乘法初始化为1，加法初始化为0，具体的部分还是看代码）

空间优化：再考虑一下，实际上两个数组的设置并不是必须的，我们从两边开始同时判断，只需要两个值用来保存乘积就可以达到想要的效果。

### 示例代码
C++:
最开始的做法，超时，也很容易看出来这种方法很麻烦。
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> res(len, 1);
        for(int i = 0; i < len; i++)
            for(int j = 0; j < len; j++){
                if(i == j)
                    continue;
                res[j] *= nums[i];
            }

        return res;
    }
};
```

构造数组：
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> res(len, 1), front(len, 1), back(len, 1);
        for(int i = 0; i < len - 1; i++){
            front[i + 1] = front[i] * nums[i];
        }

        for(int i = len - 1; i > 0 ; i--){
            back[i - 1] = back[i] * nums[i];
        }
        //上面这两种写法我一下子还真的写不出来....


        for(int i = 0; i < len; i++){
            res[i] = front[i] * back[i];
        }

        return res;
    }
};
```
上面代码用了两个循环来创造数组，不难发现这两个数组有一定的共性，完全可以用一个循环来解决。优化代码：
```cpp
class Solution {
public:
    vector<int> productExceptSelf(vector<int>& nums) {
        int len = nums.size();
        vector<int> res(len, 1);
        int front = 1, back = 1;
        for(int left = 0, right = len -1; left < len; left++, right--){
            res[left] *= front;
            res[right] *= back;
            front *= nums[left];
            back *= nums[right];
        }

        return res;
    }
};
```
但是优化后速度并没有太大的变化
