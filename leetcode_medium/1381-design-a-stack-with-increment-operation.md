## 1381. 设计一个支持增量操作的栈

2020年9月24日

### 题目

请你设计一个支持下述操作的栈。

实现自定义栈类 ``CustomStack`` ：


- ``CustomStack(int maxSize)``：用 ``maxSize`` 初始化对象，``maxSize`` 是栈中最多能容纳的元素数量，栈在增长到 ``maxSize`` 之后则不支持 ``push`` 操作。
- ``void push(int x)``：如果栈还未增长到 ``maxSize`` ，就将 ``x`` 添加到栈顶。
- ``int pop()``：弹出栈顶元素，并返回栈顶的值，或栈为空时返回 **-1** 。
- ``void inc(int k, int val)``：栈底的 ``k`` 个元素的值都增加 ``val`` 。如果栈中元素总数小于 ``k`` ，则栈中的所有元素都增加 ``val`` 。


 

**示例：**

```
输入：
["CustomStack","push","push","pop","push","push","push","increment","increment","pop","pop","pop","pop"]
[[3],[1],[2],[],[2],[3],[4],[5,100],[2,100],[],[],[],[]]
输出：
[null,null,null,2,null,null,null,null,null,103,202,201,-1]
解释：
CustomStack customStack = new CustomStack(3); // 栈是空的 []
customStack.push(1);                          // 栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.pop();                            // 返回 2 --> 返回栈顶值 2，栈变为 [1]
customStack.push(2);                          // 栈变为 [1, 2]
customStack.push(3);                          // 栈变为 [1, 2, 3]
customStack.push(4);                          // 栈仍然是 [1, 2, 3]，不能添加其他元素使栈大小变为 4
customStack.increment(5, 100);                // 栈变为 [101, 102, 103]
customStack.increment(2, 100);                // 栈变为 [201, 202, 103]
customStack.pop();                            // 返回 103 --> 返回栈顶值 103，栈变为 [201, 202]
customStack.pop();                            // 返回 202 --> 返回栈顶值 202，栈变为 [201]
customStack.pop();                            // 返回 201 --> 返回栈顶值 201，栈变为 []
customStack.pop();                            // 返回 -1 --> 栈为空，返回 -1
```

 

**提示：**


- ``1 <= maxSize <= 1000``
- ``1 <= x <= 1000``
- ``1 <= k <= 1000``
- ``0 <= val <= 100``
- 每种方法 ``increment``，``push`` 以及 ``pop`` 分别最多调用 ``1000`` 次


### 思路及代码

比较容易想到的做法是用数组模拟栈，按照指定空间初始化数组并记录当前栈顶元素对应位置，便可很简单地实现题目要求的相关操作。下面是我实现的代码。

```cpp
class CustomStack {
    int nums[1005];     // 长度小于1000
    int maxSize;
    int index;
public:
    CustomStack(int a) {
        maxSize = a;
        index = 0;
    }
    
    void push(int x) {
        if(index == maxSize){
            return ;
        }
        nums[index++] = x;
    }
    
    int pop() {
        if(index > 0){
            int tmp = nums[index-1];
            index--;
            return tmp;
        }
        else{
            return -1;
        }
    }
    
    void increment(int k, int val) {
        int len = min(k, index);
        for(int i = 0; i < len; i++){
            nums[i] += val;
        }
    }
};

/**
 * Your CustomStack object will be instantiated and called as such:
 * CustomStack* obj = new CustomStack(maxSize);
 * obj->push(x);
 * int param_2 = obj->pop();
 * obj->increment(k,val);
 */
```

但是在看过官方题解之后，发现能够让``inc``操作的时间复杂度也降低到常数，这个是我之前没有想到的。首先这种做法需要额外开辟一个数组adds，在这个数组中记录等待累加的数值，在进行增量操作时，只把待累加的数值存在这个数组的k位置。在pop时，假设当前栈顶索引为i，则应弹出nums[i]+adds[i]，而后把栈顶累加值向前传递，之后清空自身，简单来讲就是下面的操作：

```cpp
void pop(){
    int tmp = nums[i];	// 不考虑是否空栈
    tmp += adds[i];
    if(i > 0){
        adds[i-1] = adds[i];
    }
    adds[i] = 0;
    return tmp;
}
```

这样便能使所有的操作都能在常数时间内完成。
