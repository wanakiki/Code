##  Min Stack
##### 2018年2月22日17:35:16
##### 设计堆栈
***
### 题目
>Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.
设计一个支持push，pop，top，并在常量时间内检索最小元素的堆栈。

### 分析及代码
做完之后我感觉我好像误解了题目的要求，可能本应该在栈内设计好最小值，最小值个数。  
没有这样做，但是也通过了测试（这个 判断不出来😏）  
看看我的代码（一切从简.....）：
```c
typedef struct {
    int top;
    int* a;
} MinStack;

/** initialize your data structure here. */
MinStack* minStackCreate(int maxSize) {
    MinStack *obj=(MinStack*)malloc(sizeof(MinStack)); //不能赋值为空，要开辟新空间
    obj->top=0;
    obj->a=(int *)malloc(sizeof(int)*(maxSize+1));
    return obj;
}

void minStackPush(MinStack* obj, int x) {
    obj->top+=1;
    obj->a[obj->top]=x;
}

void minStackPop(MinStack* obj) {
    obj->top-=1;
}

int minStackTop(MinStack* obj) {
    return obj->a[obj->top];
}

int minStackGetMin(MinStack* obj) {
    int temp=obj->a[1];
    for(int i=1;i<=obj->top;i++){
        if(obj->a[i]<temp)
            temp=obj->a[i];
    }
    return temp;
}

void minStackFree(MinStack* obj) {
    int temp=minStackGetMin(obj);
    int flag=0;
    for(int i=1;i<obj->top;i++){
        if(obj->a[i]==temp){
            flag++;
            continue;
        }
        obj->a[i-flag]=obj->a[i];
    }
    obj->top-=flag;
}

/**
 * Your MinStack struct will be instantiated and called as such:
 * struct MinStack* obj = minStackCreate(maxSize);
 * minStackPush(obj, x);
 * minStackPop(obj);
 * int param_3 = minStackTop(obj);
 * int param_4 = minStackGetMin(obj);
 * minStackFree(obj);
 */
```
