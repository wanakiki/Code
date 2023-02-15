## 1813. 句子相似性 III

2023-01-16 18:30:18

### 题目

一个句子是由一些单词与它们之间的单个空格组成，且句子的开头和结尾没有多余空格。比方说，``"Hello World"`` ，``"HELLO"`` ，``"hello world hello world"`` 都是句子。每个单词都 **只** 包含大写和小写英文字母。

如果两个句子 ``sentence1`` 和 ``sentence2`` ，可以通过往其中一个句子插入一个任意的句子（**可以是空句子**）而得到另一个句子，那么我们称这两个句子是 **相似的** 。比方说，``sentence1 = "Hello my name is Jane"`` 且 ``sentence2 = "Hello Jane"`` ，我们可以往 ``sentence2`` 中 ``"Hello"`` 和 ``"Jane"`` 之间插入 ``"my name is"`` 得到 ``sentence1`` 。

给你两个句子 ``sentence1`` 和 ``sentence2`` ，如果 ``sentence1`` 和``sentence2`` 是相似的，请你返回 ``true`` ，否则返回 ``false`` 。

 

**示例 1：**

```
输入：sentence1 = "My name is Haley", sentence2 = "My Haley"
输出：true
解释：可以往 sentence2 中 "My" 和 "Haley" 之间插入 "name is" ，得到 sentence1 。
```

**示例 2：**

```
输入：sentence1 = "of", sentence2 = "A lot of words"
输出：false
解释：没法往这两个句子中的一个句子只插入一个句子就得到另一个句子。
```

**示例 3：**

```
输入：sentence1 = "Eating right now", sentence2 = "Eating"
输出：true
解释：可以往 sentence2 的结尾插入 "right now" 得到 sentence1 。
```

**示例 4：**

```
输入：sentence1 = "Luky", sentence2 = "Lucccky"
输出：false
```

 

**提示：**


- ``1 <= sentence1.length, sentence2.length <= 100``
- ``sentence1`` 和 ``sentence2`` 都只包含大小写英文字母和空格。
- ``sentence1`` 和 ``sentence2`` 中的单词都只由单个空格隔开。



[LeetCode链接](https://leetcode-cn.com/problems/sentence-similarity-iii/)

### 思路及代码

双向遍历，查看遍历过的字符长度能否超过某个字符串。也可以先向一侧遍历，遇到冲突之后记录位置并从右侧位置。

```python
class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        sentence1 = sentence1.split()
        sentence2 = sentence2.split()

        len1 = len(sentence1)
        len2 = len(sentence2)


        left = 0
        while left < min(len1, len2):
            if sentence1[left] != sentence2[left]:
                break
            
            left = left + 1
        if left == min(len1, len2):
            return True

        right1 = len1 - 1
        right2 = len2 - 1
        while right1 >= 0 and right2 >= 0:
            if sentence1[right1] != sentence2[right2]:
                break
            right1 = right1 - 1
            right2 = right2 - 1
        
        if (left + (len1 - right1 - 1) >= len1) or (left + (len2 - right2 - 1) >= len2):
            return True
        else:
            return False
```