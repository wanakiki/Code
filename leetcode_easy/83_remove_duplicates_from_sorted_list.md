## Remove Duplicates from Sorted List
##### 2018年02月11日13:01:34
##### 简单的题目暴露细节问题...
***
### 题目
>Given a sorted linked list, delete all duplicates such that each element appear only once.
For example,
Given 1->1->2, return 1->2.
Given 1->1->2->3->3, return 1->2->3.
给定一个有序的链表，删除所有重复，使每个元素只出现一次。   

### 分析
由于链表是有序的，所以重复的元素一定会在一块，简单的删除链表元素的方法就可以解决这个问题。  
我开始用的办法是前后两个节点比较，由于比较一次之后指针就指向了下一个节点，对于多个相同元素的情况无法解决，最后通过对操作之后的节点二次判断的方法解决了这个问题。
### 代码
```c
struct ListNode* deleteDuplicates(struct ListNode* head) {
    struct ListNode *ptr;
        ptr=head;
        while(ptr!=NULL&&ptr->next!=NULL){ 
              //先判断ptr是否为空
            if(ptr->val==ptr->next->val) {   
                //用这种写法可以减少一个变量的定义
                ptr->next=ptr->next->next;
                continue;   
                //添加continue继续判断该节点与下节点关系
            }
            
            ptr=ptr->next;  
            //这句的作用是进行下一个节点的判断，起初把这句放在了if语句内，导致出现了问题
        }
    return head;
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

        while(head){
            if(head->val != cur->val){
                cur->next = head;
                cur = cur->next;
            }
            head = head->next;
        }
        cur->next = nullptr;
        return newhead->next;
    }
};
```