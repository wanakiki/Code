## 82. Remove Duplicates from Sorted List II
##### 2018-03-28 
##### 双指针
***
## 1.题目
>Given a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list.
>给定有序链表，要求去除其中的所有重复元素。
>
>For example,
Given 1->2->3->3->4->4->5, return 1->2->5.
Given 1->1->1->2->3, return 2->3. 

## 2.分析
与之前想到的统计法不同，这次了解到了双指针的方法，但是头节点的处理还没有写出来，睡醒补上.....

最开始尝试着去寻找一次遍历解决去头的方法，但还是失败了。
但是了解到了一个新思路，可以写一个包含单独的去头部分的代码，采用递归写法，返回f(第一个不相同的节点的指针)，另外有处理非头部重复的代码。

上面方法很好，但是感觉很难想到，采用了另一种实现的方法，设置一个**新节点**，让其下一个节点为head，  
接着，用这个节点为左指针，使用while循环，在循环中定义右指针并进行处理，最终返回新节点的next

## 3.代码
```c
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* deleteDuplicates(struct ListNode* head) {
  struct ListNode *newhead=(struct ListNode *)malloc(sizeof(struct ListNode));
  newhead->next=head;
  struct ListNode * pre=newhead;
  while(pre->next){
    struct ListNode*cur=pre->next;
    while (cur->next && cur->next->val == cur->val) {
      cur=cur->next;
    }
    if(cur!=pre->next)
      pre->next=cur->next;
    else
      pre=pre->next;
  }
  return newhead->next;
}
```

```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:
    ListNode* deleteDuplicates(ListNode* head) {
        ListNode* newhead = new ListNode(-200);
        ListNode* cur = newhead;
        ListNode* last = newhead;
        bool flag = true;
        bool need_del = false;

        while(head){
            if(cur->val == head->val){
                need_del = true;
                flag = false;
            }
            else{
                flag = true;
            }

            if(flag){
                if(need_del){
                    cur = head;
                    last->next = cur;
                    need_del = false;
                }
                else{
                    cur->next = head;
                    last = cur;
                    cur = cur->next;
                }
                flag = false;
            }
            head = head->next;
        }
        // 最后判断
        if(need_del){
            last->next = nullptr;
        }
        return newhead->next;
    }
};
```

看题解评论有人说得很好，做链表题目一定要舍得用变量，这个题目便是典型的容易绕进去的类型。