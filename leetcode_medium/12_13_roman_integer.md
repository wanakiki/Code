## Rome  Integer
##### 2018年2月25日22:20:05
##### 上午重新看的
## **罗马数字维基**：  
罗马数字共有7个，即Ⅰ（1）、Ⅴ（5）、Ⅹ（10）、Ⅼ（50）、Ⅽ（100）、Ⅾ（500）和Ⅿ（1000）。按照下述的规则可以表示任意正整数。需要注意的是罗马数字中没有“0”，与进位制无关。一般认为罗马数字只用来记数，而不作演算。
- 重复数次：一个罗马数字重复几次，就表示这个数的几倍。
- 右加左减：
	- 在较大的罗马数字的右边记上较小的罗马数字，表示大数字加小数字。
	- 在较大的罗马数字的左边记上较小的罗马数字，表示大数字减小数字。
	- 左减的数字有限制，仅限于I、X、C。比如45不可以写成VL，只能是XLV
	- 但是，左减时不可跨越一个位值。比如，99不可以用IC（ {\displaystyle 100-1} 100-1）表示，而是用XCIX（ {\displaystyle [100-10]+[10-1]} [100-10]+[10-1]）表示。（等同于阿拉伯数字每位数字分别表示。）
	- 左减数字必须为一位，比如8写成VIII，而非IIX。
	- 右加数字不可连续超过三位，比如14写成XIV，而非XIIII。（见下方“数码限制”一项。）
-加线乘千：
	- 在罗马数字的上方加上一条横线或者加上下标的Ⅿ，表示将这个数乘以1000，即是原数的1000倍。
	- 同理，如果上方有两条横线，即是原数的1000000（ {\displaystyle 1000^{2}} 1000^{{2}}）倍。
- 数码限制：
	- 同一数码最多只能连续出现三次，如40不可表示为XXXX，而要表示为XL。
	- 例外：由于IV是古罗马神话主神朱庇特（即IVPITER，古罗马字母里没有J和U）的首字，因此有时用IIII代替IV。

>**题目：**
给定一个整数，将其转换为罗马数字。
输入保证在1到3999的范围内。

### 代码
```c
#include <stdio.h>
#include<string.h>
char *TurnRome(int a) {
  char Rome1[10][6]={"","I","II","III","IV","V","VI","VII","VIII","IX"};
  char Rome2[10][6]={"","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"};
  char Rome3[10][6]={"","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"};
  char Rome4[4][6]={"","M","MM","MMM"};
  int  zu[4]={0};
  for(int i=0;i<4;i++){
    zu[i]=a%10;
    a/=10;
  }
//可以考虑递归输入，还有更高一级的数组形式
//但是返回一个数组的问题还没有解决  
//printf("%s%s%s%s",Rome4[zu[3]],Rome3[zu[2]],Rome2[zu[1]],Rome1[zu[0]]);
//加入字符串链接函数，做到了返回值为字符串,但是提交还是个问题....
  static char str[16]={0};
  strcat(str,Rome4[zu[3]]);
  strcat(str,Rome3[zu[2]]);
  strcat(str,Rome2[zu[1]]);
  strcat(str,Rome1[zu[0]]);
  return str;
}
int main()
{
  int a;
  scanf("%d",&a );
  printf("%s\n",TurnRome(a));
}
```
### PS
尽管在``leetcode``交不上，但是我是对的
****
****


## 罗马转数字（2018年1月28日21:06:46）
***
>给定一个罗马数字，将其转换为整数。
输入保证在1到3999的范围内。

### 代码（绝壁可以简化）
```c
#include <stdio.h>

int change(char a){
  int temp=0;
  switch (a) {
    case 'I':temp=1;break;
    case 'V':temp=5;break;
    case 'X':temp=10;break;
    case 'L':temp=50;break;
    case 'C':temp=100;break;
    case 'D':temp=500;break;
    case 'M':temp=1000;
  }
  return temp;
}

int romanToInt(char *s){
  int k=0,num=0,num_temp=0;
  while (s[k]!='\0')
    k++;
  for(int i=0;i<k-1;i++){
      int temp=change(s[i]);
      //注意字符直接比较的问题，此处  s[i] 与change(s[i])不等价

      //此处为废物代码↓↓↓
      /*if(i==k-2){
        num_temp+=temp;
        num+=num_temp;
        break;
      }*/
      
      if(change(s[i])==change(s[i+1])){
        num_temp+=temp;
        if(i==k-2)
          num+=num_temp;
        }
      if(change(s[i])<change(s[i+1])){
        num_temp+=temp;
        num-=num_temp;
        num_temp=0;
      }
      if(change(s[i])>change(s[i+1])){
        num_temp+=temp;
        num+=num_temp;
        num_temp=0;
        }
      //printf("%d\n",num );
  }
  num+=change(s[k-1]);
  //printf("%d\n",num );
  return num;
}

int main()
{
  char Rome[]={0};
  gets(Rome);
  printf("%d\n", romanToInt(Rome));
}
```
