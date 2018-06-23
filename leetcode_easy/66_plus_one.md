## Plus One
##### 2018年02月10日19:17:36
##### 相对简单的题目，只是题目描述不那么清楚
***
### 题目
>Given a non-negative integer represented as a non-empty array of digits, plus one to the integer.
You may assume the integer do not contain any leading zero, except the number 0 itself.
The digits are stored such that the most significant digit is at the head of the list.
C：
Return an array of size *returnSize.
 Note: The returned array must be malloced, assume caller calls free().
### 分析
先解释下难懂的题目：  
输入的数组表示为一个整数，我们要对这个整数进行加一操作。``*returnSzie``要求我们改变这个指针指向的值为加一后的整数数组长度。  
还有就是这个题目需要新申请空间的情况只有数组全是九，返回数组除了首位是一其他全是零这种相对固定的情况。
### 代码
```c
int* plusOne(int* digits, int digitsSize, int* returnSize) {
    int temp=1; //该位实际值,除十得到进位；
    for(int i=digitsSize-1;i>=0;i--){
        temp+=digits[i];
        digits[i]=temp%10;
        temp/=10;
    }
	//如果首位需要进位↓↓↓
    if(temp==1){
        *returnSize=digitsSize+1;
        int *num=(int *)malloc((digitsSize+1)*sizeof(int));
        num[0]=1;
        while(digitsSize>=1){
            num[digitsSize]=0;
            digitsSize--;
        }
        return num;
    }
    else{
        *returnSize=digitsSize;
        return digits;
    }
}
```
