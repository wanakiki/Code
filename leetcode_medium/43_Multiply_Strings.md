## 43. Multiply Strings
##### 2018-03-08
***
## 1.题目
>Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2.

>Note:
>
> 1. The length of both num1 and num2 is < 110.
> 2. Both num1 and num2 contains only digits 0-9.
> 3. Both num1 and num2 does not contain any leading zero.   
> 4. You must not use any built-in BigInteger library or convert the inputs to integer directly.  
>
>假设两个非负数整数num1和num2表示为字符串，则返回num1和num2的乘积。

## 2.解法
两个数相乘，结果的长度不可能超过这两个数长度的和，所以可以用一个长为两长度之和的整型数组存储各元素相乘的结果。将整型数组初始化为零，之后根据最高位是否为零分情况赋值给要返回的字符串。  

细节在于存储数组元素大于9时的处理，以及存储数组参数的确定。

## 3.代码
```c
char * multiply(char*num1,char*num2){
        if(*num1=='0' || *num2=='0')
            return "0";	//0时返回零

	//开辟存储数组并初始化
        int l1=strlen(num1),l2=strlen(num2);
        int nums[l1+l2];
        for(int i=0;i<l1+l2;i++)
                nums[i]=0;

        char *res;
        int index=0;    //操作乘积数组
        int temp=0;     //暂存乘积
        for(int i=l1-1;i>=0;i--)
                for(int j=l2-1;j>=0;j--){
                        temp=(num1[i]-'0')*(num2[j]-'0');
                        index=l2-1-j+l1-1-i;
                        nums[index]+=temp;
			
			//大于九时的处理，需要考虑两次，并且在每次循环后判断一次
                        if(nums[index]>9){
                                nums[index+1]+=nums[index]/10;
                                nums[index]%=10;
                                if(nums[index+1]>9){
                                        nums[index+2]+=nums[index+1]/10;
                                        nums[index+1]%=10;
                                }
                        }       //由于是分层计算，不会出现三位数的情况
                }

        if(nums[l1+l2-1]==0)
                index=l1+l2;
        else
                index=l1+l2+1;
        res=malloc(sizeof(char)*index);
        char *ptr=res;
	
	//返回数组的构建
        for(int i=index-2;i>=0;i--){
                *ptr=nums[i]+48;
                ptr++;
                if(i==0)
                        *ptr='\0';
        }
        return res;
}
```
