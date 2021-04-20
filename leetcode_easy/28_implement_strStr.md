## Implement strStr()
##### 2018年02月06日21:38:57
##### 记得考虑``""``
***
### 题目
>Implement strStr().  
Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.  
 在干草堆中返回第一针的指数，如果针不是干草堆的一部分，则返回-1。（神奇的干草堆......）
### Example
```
Input: haystack = "hello", needle = "ll"
Output: 2  
Input: haystack = "aaaaa", needle = "bba"
Output: -1
```
### 分析
检测字符串从哪位开始与给定字符串相同，如果找不到就返回-1，我的做法是用循环将needle第一个元素逐个与字符串比较，找到之后在进行判断，之后返回。
**注意，不需要判断``\0``，needle为``""``的情况直接返回0。**

### 代码
```c
int strStr(char*haystack,char*needle){
        if( needle=="")
                return 0;
        for(int i=0;haystack[i]!='\0';i++){
                if(haystack[i]==needle[0]){
                        int j=0;
                        while(needle[j]!='\0'){
                                if(haystack[i+j]==needle[j]){
                                        if(needle[j+1]=='\0')
                                                return i;
                                        j++;
                                        continue;
                                }
                                else
                                        break;
                        }
                }
        }
        return -1;  //正常结束循环代表无匹配值
}
```
代码有点乱，但是解决了问题，现在还没来得及看别人的方法。


kmp算法练习：

```cpp
class Solution {
public:
    int strStr(string haystack, string needle) {
        int m = needle.size();
        if(m == 0)  return 0;

        string s = needle + '#' + haystack;
        int len = s.size();
        vector<int> p(len, 0);

        for(int i = 1; i < len; i++){
            int j = p[i-1];
            while(1){
                if(s[i] == s[j]){
                    p[i] = j + 1;
                    break;
                }
                if(j == 0){
                    j -= 1;
                    break;
                }
                j = p[j - 1];
            }
            if(j < 0){
                p[i] = 0;
            }
            // for(auto c : s){
            //     cout << c << ' ';
            // }
            // cout << endl;
            // for(auto c : p){
            //     cout << c << ' ';
            // }
            // cout << endl;
            if(p[i] == m){
                return i - m * 2;   // i - m + 1 - (m + 1)
            }
        }
        return -1;
    }
};
```