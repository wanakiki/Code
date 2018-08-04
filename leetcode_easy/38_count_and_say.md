## Count And Say
##### 2018年02月07日22:07:09
##### 这道题暴露了很多问题.....
*****
题目折腾了一天，怎么都检查不出来自己的错误，尽管现在换个方法已经解决了，但是还谈不上完全明白。
原来的问题慢慢解决。
### 经验教训
- 函数的返回值不能为局部变量，因为函数结束后相关内存区域就会被释放。可以用全局变量和``static``避免
- 统计相同元素个数的题目，前后直接比较的效果好于定义一个暂存变量
- C语言定义的字符数组不能用``a = ""``直接赋值，但是可以通过``strcpy(a,"")``达到目的
- 字符串连接函数``strcat``可以用来连接两个字符串

### 代码
参照的如下代码，但是我的做法是定义了暂存变量用于比较，没下面这种方法简单。
```c
#define maxn 10005
char s[maxn], t[maxn];
//定义全局变量
char* countAndSay(int n) {

    strcpy(s, "1");
    strcpy(t, "");
    int cnt = 1;
    char tmp[3];
    for(int i = 2;i <= n;i++){
        int len = strlen(s);
        for(int j = 0;j < len;j++){
            if(s[j] == s[j + 1]){
                cnt++;
            }else {
                tmp[0] = cnt + '0';
                tmp[1] = s[j];
                tmp[2] = '\0';
                strcat(t, tmp);
                cnt = 1;
            }
        }
        strcpy(s, t);
        strcpy(t, "");
    }
    return s;
}
```

Python3（2018年8月4日）：

```py
class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        res = [1]
        kind = 0
        num = 0
        while(n -1 ):
            n -= 1
            temp = res
            res = []
            for i in range(len(temp)):
                if i == 0:
                    kind = temp[i]
                    num += 1
                    continue
                if temp[i] == temp[i-1]:
                    num += 1
                else:
                    res.append(num)
                    res.append(kind)
                    kind = temp[i]
                    num = 1
            if not num == 0:
                res.append(num)
                res.append(kind)
                num = 0
        return "".join('%s' %id for id in res)
```

整数无法直接转化为字符串，需要先转化为字符。另外这个题目可以直接用str

```py
class Solution:
     def countAndSay(self, n):
        s = '1'
        for _ in range(n-1):
            let, temp, count = s[0], '', 0
            for l in s:
                if let == l:
                    count += 1
                else:
                    temp += str(count)+let
                    let = l
                    count = 1
            temp += str(count)+let
            s = temp
        return s
```
