## 445. 两数相加 II

2020年4月14日4

### 题目

给你两个 非空 链表来代表两个非负整数。数字最高位位于链表开始位置。它们的每个节点只存储一位数字。将这两数相加会返回一个新的链表。

你可以假设除了数字 0 之外，这两个数字都不会以零开头。

进阶：

如果输入链表不能修改该如何处理？换句话说，你不能对列表中的节点进行翻转。

 

示例：
```no
输入：(7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
输出：7 -> 8 -> 0 -> 7
```
来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/add-two-numbers-ii

### 代码

链表中数字的顺序与计算顺序是相反的，所以可以将数据先保存在栈中，之后再顺序处理。另外，一般逆序处理都会用到栈。

我的实现方式是使用头插法链表，计算结果时不需要额外反转。另外因为在while循环中多次判断了栈是否为空，在两个链表的长度相差过大时会导致不必要的操作。（但是这样代码简单

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
class Solution {
public:
    // 在头部插入元素
    void insertNode(ListNode*& root, int val){
        ListNode* tmp = new ListNode(val);
        tmp->next = root;
        root = tmp;
    }
    ListNode* addTwoNumbers(ListNode* l1, ListNode* l2) {
        stack<int> stk1, stk2;
        ListNode* res = NULL;
        while(l1 != NULL){
            stk1.push(l1->val);
            l1 = l1->next;
        }
        while(l2 != NULL){
            stk2.push(l2->val);
            l2 = l2->next;
        }

        int tmp = 0;
        while(tmp || !stk1.empty() || !stk2.empty()){
            if(!stk1.empty()){
                tmp += stk1.top();
                stk1.pop();
            }
            if(!stk2.empty()){
                tmp += stk2.top();
                stk2.pop();
            }
            insertNode(res, tmp%10);
            tmp /= 10;
        }
        return res;
    }
};
```