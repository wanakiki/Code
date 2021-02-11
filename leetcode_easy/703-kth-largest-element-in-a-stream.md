## 789. 数据流中的第 K 大元素

2021-02-11 11:55:41

### 题目

设计一个找到数据流中第 ``k`` 大元素的类（class）。注意是排序后的第 ``k`` 大元素，不是第 ``k`` 个不同的元素。

请实现 ``KthLargest`` 类：


- ``KthLargest(int k, int[] nums)`` 使用整数 ``k`` 和整数流 ``nums`` 初始化对象。
- ``int add(int val)`` 将 ``val`` 插入数据流 ``nums`` 后，返回当前数据流中 第 ``k`` 大的元素。

**示例：**

```
输入：
["KthLargest", "add", "add", "add", "add", "add"]
[[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
输出：
[null, 4, 5, 5, 8, 8]

解释：
KthLargest kthLargest = new KthLargest(3, [4, 5, 8, 2]);
kthLargest.add(3);   // return 4
kthLargest.add(5);   // return 5
kthLargest.add(10);  // return 5
kthLargest.add(9);   // return 8
kthLargest.add(4);   // return 8
```

 
**提示：**


- ``1 <= k <= 10<sup>4</sup>``
- ``0 <= nums.length <= 10<sup>4</sup>``
- ``-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup>``
- ``-10<sup>4</sup> <= val <= 10<sup>4</sup>``
- 最多调用 ``add`` 方法 ``10<sup>4</sup>`` 次
- 题目数据保证，在查找第 ``k`` 大元素时，数组中至少有 ``k`` 个元素



[LeetCode链接](https://leetcode-cn.com/problems/kth-largest-element-in-a-stream/)

### 思路及代码

topk问题，用最小堆来实现。

```cpp
class myheap {
public:
    vector<int> nums;
    int size;
    myheap(){
        size = 0;
    }

    int get_size(){
        return size;
    }

    int get_top(){
        return nums[0];
    }

    bool cmp(int aim, int cur){
        return nums[aim] > nums[cur];
    }

    int pop(){
        int tmp = nums[0];
        swap(nums[0], nums[size - 1]);
        size -= 1;
        shift_down(0);
        return tmp;
    }

    void shift_down(int index){
        // 使堆顶的较大节点下移
        
        // 若当前节点有子节点
        while(index * 2 + 1 < size){
            int smallest = index;
            int left = index * 2 + 1;
            int right = index * 2 + 2;

            if(cmp(smallest, left)){
                smallest = left;
            }
            // 必须存在右节点才能进行判断
            if(right < size && cmp(smallest, right)){
                smallest = right;
            }

            if(smallest == index){
                break;
            }
            else{
                swap(nums[index], nums[smallest]);
                index = smallest;
            }
        }
        return ;
    }

    int add(int val){
        if(nums.size() > size){
            nums[size] = val;
        }
        else{
            nums.push_back(val);
        }
        size++;

        shift_up(size-1);   // 新节点插入到尾部 之后向上调整
        return nums[0];
    }

    void shift_up(int index){
        // 使较小值移动到顶端
        while((index - 1) / 2 >= 0){
            if(index == 0){
                return ;
            }

            int parent = (index - 1) / 2;
            if(cmp(index, parent)){
                break;
            }
            swap(nums[index], nums[parent]);
            index = parent;
        }
        return ;
    }
};
class KthLargest {
public:
    int max_size = 0;
    myheap hp;

    KthLargest(int k, vector<int>& nums) {
        max_size = k;
        for(auto i : nums){
            add(i);
        }    
    }
    
    int add(int val) {
        hp.add(val);
        if(hp.get_size() > max_size){
            hp.pop();
        }
        return hp.get_top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */
 ```

 自己实现的堆结构，运行起来稍微慢一些。