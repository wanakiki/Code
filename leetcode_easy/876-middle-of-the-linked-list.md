## 876. 链表的中间结点

2020年3月23日

### 题目

给定一个带有头结点 head 的非空单链表，返回链表的中间结点。

如果有两个中间结点，则返回第二个中间结点。

 
示例 1：
```no
输入：[1,2,3,4,5]
输出：此列表中的结点 3 (序列化形式：[3,4,5])
返回的结点值为 3 。 (测评系统对该结点序列化表述是 [3,4,5])。
注意，我们返回了一个 ListNode 类型的对象 ans，这样：
ans.val = 3, ans.next.val = 4, ans.next.next.val = 5, 以及 ans.next.next.next = NULL.
```
示例 2：
```no
输入：[1,2,3,4,5,6]
输出：此列表中的结点 4 (序列化形式：[4,5,6])
由于该列表有两个中间结点，值分别为 3 和 4，我们返回第二个结点。
```

提示：

- 给定链表的结点数介于 1 和 100 之间。

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/middle-of-the-linked-list

### 代码

目标是找到链表的中间节点，可以使用双指针的方法，快指针的移动速度是慢指针的二倍，当快指针移动到链表末尾时，慢指针的位置就刚好在链表的中间。

算法时间复杂度为O(n)，执行用时：0ms，在所有C++提交中击败了100.00%的用户，内存消耗：83MB，在所有C++提交中击败了88.19%的用户。

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
    ListNode* middleNode(ListNode* head) {
        ListNode* left = head;
        ListNode* right = head;
        bool flag = true;
        while(right){
            right = right->next;
            flag = !flag;
            if(flag){
                left = left->next;
            }
        }
        return left;
    }
};
```