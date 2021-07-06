## 1533. 点菜展示表

2021-07-06 12:33:04

### 题目

给你一个数组 ``orders``，表示客户在餐厅中完成的订单，确切地说， orders[i]=[customerName<sub>i</sub>,tableNumber<sub>i</sub>,foodItem<sub>i</sub>] ，其中 customerName<sub>i</sub> 是客户的姓名，tableNumber<sub>i</sub> 是客户所在餐桌的桌号，而 foodItem<sub>i</sub> 是客户点的餐品名称。

请你返回该餐厅的 **点菜展示表**<em> 。</em>在这张表中，表中第一行为标题，其第一列为餐桌桌号 &ldquo;Table&rdquo; ，后面每一列都是按字母顺序排列的餐品名称。接下
来每一行中的项则表示每张餐桌订购的相应餐品数量，第一列应当填对应的桌号，后面依次填写下单的餐品数量。

注意：客户姓名不是点菜展示表的一部分。此外，表中的数据行应该按餐桌桌号升序排列。



**示例 1：**

```
输入：orders = [["David","3","Ceviche"],["Corina","10","Beef Burrito"],["David","3","Fried Chicken"],["Carla","5","Water"],["Carla","5","Ceviche"],["Rous","3","Ceviche"]]
输出：[["Table","Beef Burrito","Ceviche","Fried Chicken","Water"],["3","0","2","1","0"],["5","0","1","0","1"],["10","1","0","0","0"]]
解释：
点菜展示表如下所示：
Table,Beef Burrito,Ceviche,Fried Chicken,Water
3    ,0           ,2      ,1            ,0
5    ,0           ,1      ,0            ,1
10   ,1           ,0      ,0            ,0
对于餐桌 3：David 点了 "Ceviche" 和 "Fried Chicken"，而 Rous 点了 "Ceviche"
而餐桌 5：Carla 点了 "Water" 和 "Ceviche"
餐桌 10：Corina 点了 "Beef Burrito"
```

**示例 2：**

```
输入：orders = [["James","12","Fried Chicken"],["Ratesh","12","Fried Chicken"],["Amadeus","12","Fried Chicken"],["Adam","1","Canadian Waffles"],["Brianna","1","Canadian Waffles"]]
输出：[["Table","Canadian Waffles","Fried Chicken"],["1","2","0"],["12","0","3"]]
解释：
对于餐桌 1：Adam 和 Brianna 都点了 "Canadian Waffles"
而餐桌 12：James, Ratesh 和 Amadeus 都点了 "Fried Chicken"
```

**示例 3：**

```
输入：orders = [["Laura","2","Bean Burrito"],["Jhon","2","Beef Burrito"],["Melissa","2","Soda"]]
输出：[["Table","Bean Burrito","Beef Burrito","Soda"],["2","1","1","1"]]
```



**提示：**


- ``1 <= orders.length <= 5 * 10^4``
- ``orders[i].length == 3``
- ``1 <= customerName<sub>i</sub>.length, foodItem<sub>i</sub>.length <= 20``
- ``customerName<sub>i</sub>`` 和 ``foodItem<sub>i</sub>`` 由大小写英文字母及空格字符 ``' '`` 组成。
- ``tableNumber<sub>i</sub>`` 是 ``1`` 到 ``500`` 范围内的整数。



[LeetCode链接](https://leetcode-cn.com/problems/display-table-of-food-orders-in-a-restaurant/)

### 思路及代码

用集合存储菜名，用自带排序的``map<int, unordered_map<string ,int>>``存储每桌的点菜情况，注意索引为整型才能得到争取的排序结果。

由于每桌不一定点了所有类型的菜，可以通过哈希表存储菜名对应结果数组中列的索引。


```cpp
class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        set<string> foodName;
        map<int, unordered_map<string, int>> hash;
        vector<vector<string>> res;

        for(auto order : orders){
            foodName.emplace(order[2]);

            hash[stoi(order[1])][order[2]] ++;
        }

        // 获取首行、菜名及索引对应关系
        int len = foodName.size() + 1;
        unordered_map<string, int> foodIndex;   // 保存菜名和索引的对应关系

        res.push_back(vector<string>(len));
        res[0][0] = "Table";
        int cur = 1;
        for(auto name : foodName){
            foodIndex[name] = cur;
            res[0][cur++] = name;
        }

        // 保存每桌信息
        int row = 1;
        for(auto table : hash){
            res.push_back(vector<string>(len, "0"));
            res[row][0] = to_string(table.first);

            for(auto name : table.second){
                res[row][foodIndex[name.first]] = to_string(name.second);
            }
            row++;
        }

        return res;
    }
};
```

之前周赛时的解法：

```cpp
class Solution {
public:
    vector<vector<string>> displayTable(vector<vector<string>>& orders) {
        set<string> items;
        vector<map<string,int>> tables(501);
        for(int i = 0; i < orders.size(); i++){
            items.insert(orders[i][2]);
            tables[atoi(orders[i][1].c_str())][orders[i][2]]++;
        }
        vector<vector<string>> res;
        res.push_back(vector<string>());
        res[0].push_back("Table");
        for(auto i = items.begin(); i!=items.end(); i++){
            res[0].push_back(*i);
        }
        
        int cur = 0;
        // 针对每桌
        for(int i = 1; i < 501; i++){
            if(!tables[i].empty()){
                cur++;
                res.push_back(vector<string>());
                res[cur].push_back(to_string(i));
                
                for(int j = 1; j < res[0].size(); j++){
                    auto it = tables[i].find(res[0][j]);
                    if(it != tables[i].end()){
                        int num = it->second;
                        res[cur].push_back(to_string(num));
                    }
                    else{
                        res[cur].push_back(to_string(0));
                    }
                }
                
            }
        }
        return res;
    }
};
```