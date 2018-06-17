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
