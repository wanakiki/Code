## 148. Sort List
##### 2018-05-21 23:02:47
##### 链表排序
***
## 题目
Sort a linked list in O(n log n) time using constant space complexity.

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
因为之前有过在链表前面设置一个空头的经历，也算是比较简单的写完了这道题目。将当前遍历到的节点值与新链表的两个节点值比较后插入，遍历完之后就解决了这个问题。但是发现运行速度还是不那么理想。
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
    ListNode* sortList(ListNode* head) {
        ListNode * ptr= new ListNode(INT_MIN),*new_head,*temp;
        while(head){
            new_head=ptr;
            while(new_head){
                temp=new_head->next;
                if(new_head->next == NULL){
                    new_head->next=head;
                    head=head->next;
                    new_head->next->next=NULL;
                    break;
                }
                else{
                    if(head->val >= new_head->val  && head->val < new_head->next->val){
                        new_head-> next=head;
                        head=head->next;
                        new_head->next->next=temp;
                        break;
                    }
                    else
                        new_head = new_head->next;
                }
            }
            //head = head->next;
        }
        return ptr->next;
    }
};
```

下面是目前leetcode上面最快的方法，将链表储存到一个vector中排序后还原链表。这个人还写了一个比较奇怪的 auto ，里面加速了c++的输出。
```cpp
/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode(int x) : val(x), next(NULL) {}
 * };
 */
static auto x = []() {
	std::ios::sync_with_stdio(false);
	std::cin.tie(NULL);
	return 0;
}();


class Solution {
public:
   ListNode* sortList(ListNode* head)
	{
		vector<int> vec;
		ListNode *ln = head;
		for (; ln != NULL; ln = ln->next)
		{
			vec.push_back(ln->val);
		}

		sort(vec.begin(), vec.end());

		ln = head;
		for (auto i : vec)
		{
			ln->val = i;
			ln = ln->next;
		}

		return head;
	}
};
```


#### 2020年11月21日

如果想要完全按照题目的要求，使用常数空间来做这个题目的话，需要使用自底向上的归并排序做法。

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
    ListNode* sortList(ListNode* head) {
        ListNode* newhead = new ListNode(0, head);
        ListNode* cur = newhead;
        int cur_len = 1;
        int len = 0;
        // 计算长度
        while(head){
            len++;
            head = head->next;
        }
        for(cur_len = 1; cur_len < len; cur_len <<= 1){
            ListNode* last = newhead;
            ListNode* cur = newhead->next;
            while(cur){
                ListNode* head1 = cur;
                ListNode* tmp1 = head1;
                for(int i = 1; i < cur_len && tmp1->next; i++){
                    tmp1 = tmp1->next;
                }
                ListNode* head2 = tmp1->next;
                tmp1->next = nullptr;
                tmp1 = head2;
                for(int i = 1; i < cur_len && tmp1 && tmp1->next; i++){
                    tmp1 = tmp1->next;
                }
                // 上面循环的终止条件有两种，tmp1本身为空，tmp1->next为空
                ListNode* tmp2 = nullptr;
                if(tmp1){
                    tmp2 = tmp1->next;
                    tmp1->next = nullptr;
                }

                ListNode* merged = mergeList(head1, head2);
                last->next = merged;
                while(last && last->next){
                    last = last->next;
                }
                cur = tmp2;
            }
        }
        return newhead->next;
    }
    ListNode* mergeList(ListNode* left, ListNode* right){
        ListNode* newhead = new ListNode(0);
        ListNode* cur = newhead;
        while(left && right){
            if(left->val < right->val){
                cur->next = left;
                left = left->next;
                cur = cur->next;
            }
            else{
                cur->next = right;
                right = right->next;
                cur = cur->next;
            }
        }

        if(left){
            cur->next = left;
        }
        else{
            cur->next = right;
        }
        return newhead->next;
    }
};
```