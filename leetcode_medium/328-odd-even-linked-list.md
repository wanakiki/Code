## 328. 奇偶链表

2020年11月14日

### 题目

给定一个单链表，把所有的奇数节点和偶数节点分别排在一起。请注意，这里的奇数 
节点和偶数节点指的是节点编号的奇偶性，而不是节点的值的奇偶性。

请尝试使用原地算法完成。你的算法的空间复杂度应为 O(1)，时间复杂度应为 O(nodes)，nodes 为节点总数。

**示例 1:**

```
输入: 1->2->3->4->5->NULL
输出: 1->3->5->2->4->NULL
```

**示例 2:**

```
输入: 2->1->3->5->6->4->7->NULL
输出: 2->3->6->7->1->5->4->NULL
```

**说明:**


- 应当保持奇数节点和偶数节点的相对顺序。
- 链表的第一个节点视为奇数节点，第二个节点视为偶数节点，以此类推。

### 思路及代码

#### 奇节点前插

遍历链表，将所有的奇节点放到链表的前面，其余节点的位置不变。

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
    ListNode* oddEvenList(ListNode* head) {
        if(!head){
            return head;
        }
        ListNode* left = head;
        ListNode* cur = head->next;     //指向需要修改节点的前一个位置
        while(1){
            if(cur && cur->next){
                // 奇数节点前插，画图更容易理解
                ListNode* tmp = left->next;
                left->next = cur->next;
                cur->next = cur->next->next;
                cur = cur->next;
                left = left->next;
                left->next = tmp;
            }
            else{
                break;
            }
        }
        return head;
    }
};
```

#### 奇偶节点分离再合并

这是官方题解给出的方法，比我上面提到的方法更易于实现。建立奇偶链表头，之后遍历链表，将节点插入到对应链表头的后面，最后再合并。

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
    ListNode* oddEvenList(ListNode* head) {
        if(!head){
            return head;
        }
        ListNode* odd = head;
        ListNode* evenHead = head->next;
        bool flag = true;
        ListNode* even = head->next;
        while(even && even->next){
            odd->next = even->next;
            odd = odd->next;
            even->next = odd->next;
            even =  even->next;
        }
        odd->next = evenHead;
        return head;
    }
};
```