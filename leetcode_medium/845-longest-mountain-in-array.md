## 845. 数组中的最长山脉

2020年10月25日

### 题目

我们把数组 A 中符合下列属性的任意连续子数组 B 称为“<em>山脉”</em>：


- ``B.length >= 3``
- 存在 ``0 < i < B.length - 1`` 使得 ``B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]``


（注意：B 可以是 A 的任意子数组，包括整个数组 A。）

给出一个整数数组 ``A``，返回最长 *“山脉”* 的长度。

如果不含有“山脉”则返回 ``0``。



**示例 1：**

```
输入：[2,1,4,7,3,2,5]
输出：5
解释：最长的 “山脉” 是 [1,4,7,3,2]，长度为 5。
```

**示例 2：**

```
输入：[2,2,2]
输出：0
解释：不含 “山脉”。
```



**提示：**


- ``0 <= A.length <= 10000``
- ``0 <= A[i] <= 10000``


### 思路及代码

#### 双向扫描

从左向右扫描，统计连续递增区间的长度，再从右向左扫描，统计连续递增区间的长度。之后遍历扫描结果，当某处左右递增区间长度均大于0时，该点满足山脉数组的山峰条件，山脉数组的长度为 ``left[i] + right[i] + 1``。

```cpp
class Solution {
public:
    int longestMountain(vector<int>& A) {
        int len = A.size();
        if(len < 3){
            return 0;
        }
        vector<int> left(len, 0);
        vector<int> right(len, 0);

        for(int i = 1; i < len; i++){
            if(A[i] > A[i-1]){
                left[i] = left[i-1] + 1;
            }
        }
        for(int j = len - 2; j >= 0; j--){
            if(A[j] > A[j+1]){
                right[j] = right[j+1] + 1;
            }
        }

        int res = 0;
        for(int i = 0; i < len; i++){
            int tmp = min(left[i], right[i]);
            if(tmp > 0){
                res = max(res, left[i] + right[i] + 1);
            }
        }
        return res;
    }
};
```

#### 遍历每个山脉

因为山脉数组有较多的限制条件，导致逐个遍历山脉数组时需要考虑很多边界条件。大致处理方法如下：

设置起点s，取变量``i = s + 1``开始判断A[i]是否大于A[i-1]，循环的终止情况有三种：

1. ``s+1``，证明当前s不满足作为山脉起点的条件
2. ``len``，上升区间延伸到数组末尾
3. ``s+1 < i < len``，当前i所在位置指向山峰之后的一个元素

当出现前两种情况后，需要直接更新起点并重新判断，出现第三种情况则需要判断后半部分是否满足下降条件：以``j = i``为起点开始判断A[j]是否小于A[j-1]，循环有三种终止情况：

1. ``i``，顶峰右侧不满足下降条件（相等）
2. ``len``，下降区间延伸到数组末尾
3. ``i < j < len``，指向山脉数组的山脚之后第一个元素

第一种情况需要更新起点位置后重新开始判断，剩余两种情况则证明找到了一个山脉数组，可以进一步计算数组长度``j - s``，因为此时j位于山脚之后的第一个元素位置，所以下次循环的起点是``j-1``。

```cpp
class Solution {
public:
    int longestMountain(vector<int>& A) {
        int len = A.size();
        int res = 0;
        if(len < 3){
            return res;
        }

        int cur = 0;    //每段的起始位置
        while(cur < len){
            int i, j;
            for(i = cur + 1; i < len; i++){
                if(A[i] <= A[i-1]){
                    break;
                }
            }

            // i为len代表上升区间一直延伸到右侧，i==cur+1代表不存在上升区间，两种情况需要更新起点
            if(i == len || i == cur + 1){
                cur = i;
                continue;
            }

            // j会停留在下一个山脉的第二个点
            for(j = i; j < len; j++){
                if(A[j] >= A[j-1]){
                    break;
                }
            }

            // j==i代表右侧不递减
            if(j == i){
                cur = j;
                continue;
            }
            res = max(res, j - cur);    // j停留位置为山脚之后的地点
            cur = j - 1;
        }
        return res;
    }
};
```

这段代码是在停电之前赶出来的，感觉应该有可以被优化的地方。