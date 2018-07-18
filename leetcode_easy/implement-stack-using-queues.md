## Implement Stack using Queues
##### 2018年6月26日
##### 用队列实现栈
***
## 题目
Implement the following operations of a stack using queues.

- push(x) -- Push element x onto stack.
- pop() -- Removes the element on top of the stack.
- top() -- Get the top element.
- empty() -- Return whether the stack is empty.

Example:
```
MyStack stack = new MyStack();

stack.push(1);
stack.push(2);  
stack.top();   // returns 2
stack.pop();   // returns 2
stack.empty(); // returns false
Notes:

You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).
```
Notes:

- You must use only standard operations of a queue -- which means only push to back, peek/pop from front, size, and is empty operations are valid.
- Depending on your language, queue may not be supported natively. You may simulate a queue by using a list or deque (double-ended queue), as long as you use only standard operations of a queue.
- You may assume that all operations are valid (for example, no pop or top operations will be called on an empty stack).

## 思路
要求用队列实现栈，已经知道队列的特点是先进先出，栈的特点是先进后出，因为栈后插入的元素都在栈的顶部，所以比较简单的方法是每插入一个元素，都将他移动到队列的最前端。

具体怎么做？队列的front函数可以访问队前的元素，pop函数可以弹出最前端的函数，我们可以设置一个循环，将队前元素压入到队中，再弹出最前端的元素，这样就达到了移动的目的，控制好循环的次数就能达到想要的结果。

另外需要注意的是，队列的pop函数并没有返回值，所以实现栈的pop函数时需要先设置变量，稍微麻烦一步。
## 示例代码
```cpp
class MyStack {
private:
     queue<int> q;
public:
    /** Initialize your data structure here. */
    MyStack() {

    }

    /** Push element x onto stack. */
    void push(int x) {
        q.push(x);
        for(int i=1;i<q.size();i++){
          q.push(q.front());
          q.pop();
        }
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        int a=q.front();
        q.pop();
        return a;
    }

    /** Get the top element. */
    int top() {
        return q.front();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return q.empty();
    }
};
/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * bool param_4 = obj.empty();
 */
```
