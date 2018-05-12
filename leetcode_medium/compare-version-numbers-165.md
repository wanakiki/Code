## 165. Compare Version Numbers
##### 2018-05-12 22:36:34
##### 比较版本号
***
## 题目
Compare two version numbers version1 and version2.
If ``version1 > version2`` return 1; if ``version1 < version2`` return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only digits and the ``.`` character.
The`` .`` character does not represent a decimal point and is used to separate number sequences.
For instance, ``2.5`` is not "two and a half" or "half way to version three", it is the fifth second-level revision of the second first-level revision.

Example 1:
```
Input: version1 = "0.1", version2 = "1.1"
Output: -1
```
Example 2:
```
Input: version1 = "1.0.1", version2 = "1"
Output: 1
```
Example 3:
```
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1
```
## 分析
这道题刚好是这学期做过的一道题，尽管印象不是很深刻，但还是很快写完了。

设置两个变量用来暂存版本号的数字（避免出现二位数），遇到点停止读入，两个都读完之后进行比较，只判断大于和小于的情况，等于不做处理，将两个暂存变量清零，同时将两个下标加一，继续进行下一轮的读入，读入结束之后返回0。
## 示例代码
```cpp
class Solution {
public:
    int compareVersion(string version1, string version2) {
        int temp = 0,temp2=0;
        int i=0, j=0;
        int len1=version1.size(), len2=version2.size();
        while(i< len1 || j<len2){   //这个条件实际上写的很模糊，但是不影响我们的函数
            while(version1[i]!='.' && i<len1)
                temp=temp*10+version1[i++]-'0';
            while(version2[j]!='.' && j<len2) //需要防止越界
                temp2=temp2*10+version2[j++]-'0';
            if(temp > temp2)
                return 1;
            if(temp < temp2)
                return -1;
            temp=temp2=0;
            i++;
            j++;    //跳过点
        }
        return 0;
    }
};
```
很简单，运行也比较快，100%
