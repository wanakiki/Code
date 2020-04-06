## 42. Trapping Rain Water
##### 2018-05-31 23:18:02
##### 第一个困难题（原因：看错了...)
***
## 题目
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

![tupian](http://www.leetcode.com/static/images/problemset/rainwatertrap.png)

The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:
```
Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
```
## 分析
我的想法是假设有一块木板，从左边压上去，如果能够闭合，下面都有水。对应的，木板的右边所接触的位置就是下一次放木板开始的位置。事实证明，这个方法是错误的...
不过我认为，如果按照这个过程，反过来操作一次，应该就是
## 示例代码
~~错误代码：~~
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int len=height.size(),index=0,h;
        int sum=0; 
        while(index<len-1){
            for(int i=index;i<len;i++){
                if(height[i]>=height[index]){
                     if(i-1>=0 && height[index-1] > height[index] )
                         h=height[i];
                    else
                        h=height[index];//这里 还自作聪明地多加了一步判断之前高度的过程
                    
                        for(int j=index;j<i;j++)
                            sum+=h-height[j];
                    index=i;
                }
            }
            index++;
        }
        return sum;
        
    }
};
```
正确代码：
```cpp
class Solution {
public:
   int trap(vector<int>& height) {
        int len=height.size(),index=0,h;
        int sum=0; 
        //正向遍历
        while(index<len-1){
            for(int i=index+1;i<len;i++){
                if(height[i]>=height[index]){
                	h=height[index];
                    for(int j=index+1;j<i;j++){
                    	sum+=h-height[j];
                    	height[j]=h;
                    }
                    index=i-1;
                    break; 
                } 
            }
            index++;
        }
        //反向遍历
        while(index>0){
        	for(int i=index-1;i>=0;i--){
				if(height[i]>=height[index]){
					h=height[index];
					for(int j=index-1;j>i;j--){
						sum+=h-height[j];
					}
					index=i+1;
					break;
				}
			}
			index--; 
		}
        return sum;
    }
};
```
*** 
##### 2018-6-2-15:55
下面是看了解析之后的做法，用的是类似双指针的做法，左右两边同时操作，更新最大高度，同时不断填满空缺。
```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        //int len=height.size();
		int l=0,r=height.size()-1;
		int l_max=0,r_max=0,sum=0;
		while(l<r){
			if(height[l]<height[r]){    //注意比较的对象是当前指向的左右两个值
				height[l]>l_max	? (l_max = height[l]) : (sum+=l_max-height[l]);
				l++;
			}
			else{
				height[r]>r_max ? (r_max = height[r]) : (sum += r_max-height[r]);
				r--;
			}
		}
		return sum; 
    }
};
```


### 2020年4月4日

两个DP获得左右最大高度，最后遍历一遍计算最终结果

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;
        vector<int> left_height(height.size(), 0);
        vector<int> right_height(height.size(), 0);

        // dp获取左右最大高度
        int tmp = 0;
        for(int i = 0; i < height.size(); i++){
            if(height[i] > tmp)
                tmp = height[i];
            left_height[i] = tmp;
        }
        tmp = 0;
        for(int i = height.size()-1; i >= 0; i--){
            if(height[i] > tmp)
                tmp = height[i];
            right_height[i] = tmp;
        }

        // 遍历一次获得最终长度
        int cur = 0;
        for(int i = 0; i < height.size(); i++){
            cur = min(left_height[i], right_height[i]);
            if(cur > height[i])
                res += cur - height[i];
        }
        return res;
    }
};
```

#### 单调栈

题解区有很多人都在讨论用单调栈来解决这个问题，看了别人的讲解自己也来写一下关于单调栈的解法。

双DP做法在计算最终结果的时候是计算每个坐标最多能盛放多少水，而单调栈的做法则是在维护栈的过程中如果发现在一个区间内能注水，那就在该区间倒上对应层数的水，实际过程中只需要遍历一次数组，计算水量的方式是计算宽和高的乘积。

栈中保存的元素有两种选择：高度、坐标，为了知道两个柱体之间的距离，本题目当中需要将坐标放入栈中保存，用坐标在height数组中获取高度。具体步骤可拆分为：

1. 判断栈是否为空，若为空则当前坐标压栈。
2. 若不为空，则将当前高度与栈顶坐标对应高度相比较。
3. 若大于栈顶元素，将栈顶元素弹出保存，判断栈是否为空，若为空则证明之前被弹出的元素为最后一个，栈中没有其他柱体能帮他接水，故应终止循环。若栈不为空，则取栈顶元素与当前遍历到的元素中较小的一个，计算新的水量。重复此过程直到栈空。
4. 当前坐标压栈。

```cpp
class Solution {
public:
    int trap(vector<int>& height) {
        int res = 0;
        stack<int> stk; // 单调栈
        for(int i = 0; i < height.size(); i++){
            while(!stk.empty() && height[i] > height[stk.top()]){
                int base = stk.top();
                stk.pop();
                if(stk.empty())
                    break;

                int h = min(height[stk.top()], height[i]) - height[base];
                int distance = i - stk.top() - 1;       // 应以更高位置的距离进行计算
                res += distance * h;
            }
            stk.push(i);
        }
        return res;
    }
};
```

