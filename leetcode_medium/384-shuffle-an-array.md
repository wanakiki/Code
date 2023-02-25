## 384. 打乱数组

2021-11-24 21:11:51

### 题目

给你一个整数数组 nums ，设计算法来打乱一个没有重复元素的数组。

实现 ``Solution`` class:


- ``Solution(int[] nums)`` 使用整数数组 ``nums`` 初始化对象
- ``int[] reset()`` 重设数组到它的初始状态并返回
- ``int[] shuffle()`` 返回数组随机打乱后的结果


 

**示例：**

```

输入
["Solution", "shuffle", "reset", "shuffle"]
[[[1, 2, 3]], [], [], []]
输出
[null, [3, 1, 2], [1, 2, 3], [1, 3, 2]]

解释
Solution solution = new Solution([1, 2, 3]);
solution.shuffle();    // 打乱数组 [1,2,3] 并返回结果。任何 [1,2,3]的排列返回的概率应该相同。例如，返回 [3, 1, 2]
solution.reset();      // 重设数组到它的初始状态 [1, 2, 3] 。返回 [1, 2, 3]
solution.shuffle();    // 随机返回数组 [1, 2, 3] 打乱后的结果。例如，返回 [1, 3, 2]
```

 

**提示：**


- ``1 <= nums.length <= 200``
- ``-10<sup>6</sup> <= nums[i] <= 10<sup>6</sup>``
- ``nums`` 中的所有元素都是 **唯一的**
- 最多可以调用 ``5 * 10<sup>4</sup>`` 次 ``reset`` 和 ``shuffle``



[LeetCode链接](https://leetcode-cn.com/problems/shuffle-an-array/)

### 思路及代码

朴素做法，循环产生随机数并判断是否已经使用。

```cpp
class Solution {
public:
    vector<int> original_num;

    Solution(vector<int>& nums) {
        original_num = nums;
    }
    
    vector<int> reset() {
        return original_num;
    }
    
    vector<int> shuffle() {
        vector<int> flag(original_num.size(), 0);
        vector<int> res(original_num.size(), 0);

        int len = original_num.size();
        int index = 0;

        while(index < len){
            // 循环产生随机数 直到查找到可以存放的数值
            while(1){
                int cur_index = rand() % len;
                // cout << cur_index << endl;
                if(flag[cur_index] == 0){
                    flag[cur_index] = 1;
                    res[index++] = original_num[cur_index];
                    break;
                }
            }
        } 
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```

洗牌算法，已经使用过的随机数不会再次使用。

```class Solution {
public:
    vector<int> original_num;

    Solution(vector<int>& nums) {
        original_num = nums;
    }
    
    vector<int> reset() {
        return original_num;
    }
    
    vector<int> shuffle() {
        vector<int> nums = original_num;
        vector<int> res;
        int rand_count = 0;
        while(rand_count < nums.size()){
            int cur = rand() % (nums.size() - rand_count);
            res.push_back(nums[cur]);

            // 交换nums中元素位置
            rand_count++;
            swap(nums[cur], nums[nums.size() - rand_count]);
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
 ```

洗牌算法修改版，参照官方题解，只需要一个数组就能完成操作。

```cpp
class Solution {
public:
    vector<int> original_num;

    Solution(vector<int>& nums) {
        original_num = nums;
    }
    
    vector<int> reset() {
        return original_num;
    }
    
    vector<int> shuffle() {
        vector<int> res = original_num;
        for(int i = 0; i < res.size() - 1; i++){
            int cur = i + rand() % (res.size() - i);
            swap(res[cur], res[i]);
        }
        return res;
    }
};

/**
 * Your Solution object will be instantiated and called as such:
 * Solution* obj = new Solution(nums);
 * vector<int> param_1 = obj->reset();
 * vector<int> param_2 = obj->shuffle();
 */
```


#### 线性同余法

https://zhuanlan.zhihu.com/p/36301602

核心思想是 ``N[x+1] = (A * N[x] + B) % M``，其中A、B、M均为常量，且可以使用随机数种子初始化``N[0]``。