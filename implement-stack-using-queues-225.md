```cpp
class MyStack {
public:
    queue stack1;
    queue stack2;
    /** Initialize your data structure here. */
    MyStack() {
        stack1 = new queue();
        stack2 = new queue();
    }

    /** Push element x onto stack. */
    void push(int x) {
      stack1,push(x);        
    }

    /** Removes the element on top of the stack and returns that element. */
    int pop() {
        while(stack1.size() != 1){
          stack2.push(stack.front());
          stack1.pop();
        }
        int temp = stack1.back();
        stack1.pop();
        while(stack2.size()){
          stack1.push(stack2.front());
          stack2.pop();
        }
        return temp;
    }

    /** Get the top element. */
    int top() {
        return stack1.back();
    }

    /** Returns whether the stack is empty. */
    bool empty() {
        return stack1.empty();
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
