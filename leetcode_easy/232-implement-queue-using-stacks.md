## 232. 用栈实现队列

2021-03-05 11:28:50

### 题目

请你仅使用两个栈实现先入先出队列。队列应当支持一般队列的支持的所有操作（``push``、``pop``、``peek``、``empty``）：

实现 ``MyQueue`` 类：


- ``void push(int x)`` 将元素 x 推到队列的末尾
- ``int pop()`` 从队列的开头移除并返回元素
- ``int peek()`` 返回队列开头的元素
- ``boolean empty()`` 如果队列为空，返回 ``true`` ；否则，返回 ``false``


 

**说明：**


- 你只能使用标准的栈操作 —— 也就是只有 ``push to top``, ``peek/pop from top``, ``size``, 和 ``is empty`` 操作是合法的。
- 你所使用的语言也许不支持栈。你可以使用 list 或者 deque（双端队列）来模拟一个栈，只要是标准 
的栈操作即可。


 

**进阶：**


- 你能否实现每个操作均摊时间复杂度为 ``O(1)`` 的队列？换句话说，执行 ``n`` 个操作的总时间复杂
度为 ``O(n)`` ，即使其中一个操作可能花费较长时间。


 

**示例：**

```
输入：
["MyQueue", "push", "push", "peek", "pop", "empty"]
[[], [1], [2], [], [], []]
输出：
[null, null, null, 1, 1, false]

解释：
MyQueue myQueue = new MyQueue();
myQueue.push(1); // queue is: [1]
myQueue.push(2); // queue is: [1, 2] (leftmost is front of the queue)
myQueue.peek(); // return 1
myQueue.pop(); // return 1, queue is [2]
myQueue.empty(); // return false
```



**提示：**


- ``1 <= x <= 9``
- 最多调用 ``100`` 次 ``push``、``pop``、``peek`` 和 ``empty``
- 假设所有操作都是有效的 （例如，一个空的队列不会调用 ``pop`` 或者 ``peek`` 操作）



[LeetCode链接](https://leetcode-cn.com/problems/implement-queue-using-stacks/)

### 思路及代码

比较容易想到的做法是，用一个栈存放正确顺序的元素（队列顺序），用另外一个栈来帮助栈中元素进行翻转。当新加入元素时，先将数据栈中所有元素pop到辅助栈中，之后让新元素加入数据栈，之后把辅助栈中所有元素pop到数据栈，这样就使得栈顶元素为较早加入的元素。

```cpp
class MyQueue {
public:
    stack<int> A;
    stack<int> B;   // B用于存储
    /** Initialize your data structure here. */
    MyQueue() {
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        while(!A.empty()){
            B.push(A.top());
            A.pop();
        }
        A.push(x);
        while(!B.empty()){
            A.push(B.top());
            B.pop();
        }
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        int x = A.top();
        A.pop();
        return x;
    }
    
    /** Get the front element. */
    int peek() {
        return A.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return A.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
 ```

但上面的做法每次加入元素都需要重复用辅助栈暂存数据的操作，现在考虑队列的特点先进先出，实际上我们只想知道先加入到队列中的元素，因此上面描述方法中每次新加入元素时的搬运元素的过程做了一些不必要的操作，每push一次，早前的元素都要被搬运一次。

由此我们可以这样做，用一个栈来存储所有加入的数据，当我们需要弹出元素时，把数据栈中所有的元素都pop到另外一个栈（输出栈）中，此时输出栈中顶部的元素是较早加入的元素，我们可以对输出栈进行正常的栈操作实现队列的特性。

当我们把输出栈中所有元素都弹出后，如果还要弹出数据，就重复从数据栈到输出栈的搬运过程，之后接着对输出栈进行操作。这样每个元素就只被搬运了一次，搬运操作只会在pop且输出栈为空时发生，该过程均摊到每次pop操作，每次操作的复杂度便为O(1)。

```cpp
class MyQueue {
public:
    stack<int> A;   // A用于记录数据
    stack<int> B;   // B用于输出
    /** Initialize your data structure here. */
    MyQueue() {
    }
    
    /** Push element x to the back of queue. */
    void push(int x) {
        A.push(x);
    }
    
    /** Removes the element from in front of queue and returns that element. */
    int pop() {
        if(B.empty()){
            while(!A.empty()){
                B.push(A.top());
                A.pop();
            }
        }
        int x = B.top();
        B.pop();
        return x;
    }
    
    /** Get the front element. */
    int peek() {
        if(B.empty()){
            while(!A.empty()){
                B.push(A.top());
                A.pop();
            }
        }
        return B.top();
    }
    
    /** Returns whether the queue is empty. */
    bool empty() {
        return A.empty() && B.empty();
    }
};

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue* obj = new MyQueue();
 * obj->push(x);
 * int param_2 = obj->pop();
 * int param_3 = obj->peek();
 * bool param_4 = obj->empty();
 */
 ```