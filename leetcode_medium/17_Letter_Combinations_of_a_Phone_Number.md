## Letter Combinations of a Phone Number
##### 2018年2月25日20:57:00
##### 递归迭代两种实现
***
### 题目
>给定一个数字字符串，返回数字可能表示的所有可能的字母组合。  
数字到字母的映射（就像在电话按钮上一样）在下面给出。  
```
1       2(abc)  3(def)
4(ghi)  5(jkl)  6(mno)
7(pqrs) 8(tuv)  9(wxyz)
*       0       #
```
例如：
```
Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```
>注意：
虽然上面的答案是按字典顺序排列的，但您的答案可以是任何您想要的顺序。

### 分析
个人递归还是不好，这个题目看到完全没有头绪，知道字符的规律却没有办法用代码实现。  递归的思路是分别考虑各种情况并存储。很难说明白，看代码。（自己也不是那么清楚）  

提交的时候发现了一个问题，网上的代码不能排除20012的情况却能提交，感觉是OJ的问题。修改了下自己的代码，同样提交成功。

出现了编译错误，一并写在注释里了
### 代码（递归）
```c
static const char* letters[10] = {"", "", "abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"};
//起初没有想到这点
void combine(int start,int end,char **combinations,char* temp,char *digits,int *index)
{
    if(start==end){
        combinations[*index]=(char*)malloc(sizeof(char)*(end));
        temp[end]='\0';
        strcpy(combinations[*index],temp);
        (*index)++;
    }
    else{
        const char *letter=letters[digits[start]-'0'];
        for(int i=0;i<strlen(letter);i++){
            temp[start]=letter[i];
            combine(start+1,end,combinations,temp,digits,index);
        }
    }
}
char** letterCombinations(char* digits, int* returnSize) {
    if (digits == NULL) {
    	return NULL;
    }
    int digitslen = strlen(digits);
    /*if (digitslen == 0) {
    	return NULL;
    }
注释的部分codeblock编译成功，但是leetcode报错
load of null pointer of type 'char *'
	*/
    int resultlen=0;
    char *digits2=digits;
    *returnSize=1;
    int index=0;
    for(int i=0;i<digitslen;i++){
            if(digits[i]>='2' &&digits[i]<='9'){
                digits2[index]=digits[i];
                index++;
                *returnSize*=strlen(letters[digits[i]-'0']);
            }
    } //排除零和一
    if(*returnSize==1)
        return NULL;
    digits2[index]='\0';
    char **combinations=(char**)malloc(sizeof(char *)*(*returnSize)); //返回字符串
    char *temp=(char *)malloc(sizeof(char)*(index));    //暂存字符串
    int index2=0;
    combine(0,index,combinations,temp,digits,&index2);
    return combinations;
    }
```
我要去反馈......
