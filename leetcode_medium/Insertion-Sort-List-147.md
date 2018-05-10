## 147. Insertion Sort List
##### 2018-05-10 23:29:02
##### 链表排序
****
##  题目
Sort a linked list using insertion sort.
![test](https://upload.wikimedia.org/wikipedia/commons/0/0f/Insertion-sort-example-300px.gif)

A graphical example of insertion sort. The partial sorted list (black) initially contains only the first element in the list.
With each iteration one element (red) is removed from the input data and inserted in-place into the sorted list

Algorithm of Insertion Sort:

1. Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
2. At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
3. It repeats until no input elements remain.

Example 1:
```
Input: 4->2->1->3
Output: 1->2->3->4
```
Example 2:
```
Input: -1->5->3->4->0
Output: -1->0->3->4->5
```
## 分析
没啥好说的.....感觉很简单，总是觉得会了但是写不对，实际上有很多种实现方式，我这种也算是比较慢的，但是好歹过了

这可是，之前的上机题目啊！！！！
## 示例代码
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
    ListNode* insertionSortList(ListNode* head) {
        ListNode * _head=new ListNode(INT_MIN), * ptr=head,* temp;
        while(ptr){
            head = _head;
            while(head){
                if(head->next == NULL || (ptr->val>=head->val && ptr->val <= head->next->val)){
                    temp=ptr->next;
                    ptr->next=head->next;
                    head->next=ptr;
                    ptr=temp;
                    break;
                }
                head=head->next;
            }

        }

        return _head->next;
    }
};
```
