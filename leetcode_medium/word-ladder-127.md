## 127. Word Ladder
##### 2018-05-22 20:03:48
##### 运用多种容器加快程序运行
***
## 题目
Given two words (beginWord and endWord), and a dictionary's word list, find the length of shortest transformation sequence from beginWord to endWord, such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list. Note that beginWord is not a transformed word.
Note:

Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
Example 1:
```
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.
```
Example 2:
```
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.
```
## 分析
这个题目queue的引入是一个比较关键的部分，因为开始的单词可能的变化有很多种情况，同时我们也不能确定哪一个是最优解，所以我们可以将所有满足条件的替换压入队列，对每种情况判断完之后将其弹出。

详细描述：将起始单词压入队列，起始长度let为1，当队列不为空时对其中的所有元素进行操作，在单词表中查找和当前操作元素相差一个字母的单词，将其压入队列，同时在单词表中删除该单词。（要注意，vector用erase删除元素之后该元素之后元素的下表都减一）
但如果查找到的单词是终止单词就应该直接返回let。
如果查找完没有发现则返回零。（因而不需要考虑单词表中没有结束单词的情况）


我并没有对单词表进行修改，但是比较快的提交里面有人将单词表变成了set或者map，加快了运行速度。

## 示例代码
```cpp
class Solution {
public:
    int ladderLength(string beginWord, string endWord, vector<string>& wordList) {
        queue<string> que;
        que.push(beginWord);
        int ret=1;
        while(!que.empty()){
            ret++;
            int len=que.size();
            for(int j=0;j<len;j++){
            string temp=que.front();
            que.pop();
            for(int i=0;i<wordList.size();i++){
                if(diff(temp,wordList[i])){
                    if(wordList[i] == endWord)
                        return ret;
                    que.push(wordList[i]);
                    wordList.erase(wordList.begin()+i);
                    i--;
                }
            }
            }
        }
        return 0;
    }
    
    static bool diff(string & a,string & b){
        int sum=0;
        for(int i=0;i<a.size();i++){
            if(a[i]!=b[i])
                sum++;
            if(sum>1)
                return false;
        }
        return sum==1;
    }
};
```
