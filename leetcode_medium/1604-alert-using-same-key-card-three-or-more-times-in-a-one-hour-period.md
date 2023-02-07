## 1604. 警告一小时内使用相同员工卡大于等于三次的人

2023-02-07 11:56:49

### 题目

力扣公司的员工都使用员工卡来开办公室的门。每当一个员工使用一次他的员工卡，安保系统会记录下员工的名字和使用时间。如果一个员工在一小时时间内使用员工卡的次数大于等于三次，这个系统会自动发布一个 **警告** 。

给你字符串数组 ``keyName`` 和 ``keyTime`` ，其中 ``[keyName[i], keyTime[i]]`` 对应一个人的名字和他在 **某一天** 内使用员工卡的时间。

使用时间的格式是 **24小时制** ，形如** "HH:MM"** ，比方说 ``"23:51"`` 和 ``"09:49"`` 。

请你返回去重后的收到系统警告的员工名字，将它们按 **字典序****升序 **排序后返回。

请注意 ``"10:00"`` - ``"11:00"`` 视为一个小时时间范围内，而 ``"23:51"`` - ``"00:10"`` 不被视为一小时内，因为系统记录的是某一天内的使用情况。

 

**示例 1：**

```
输入：keyName = ["daniel","daniel","daniel","luis","luis","luis","luis"], keyTime = ["10:00","10:40","11:00","09:00","11:00","13:00","15:00"]
输出：["daniel"]
解释："daniel" 在一小时内使用了 3 次员工卡（"10:00"，"10:40"，"11:00"）。
```

**示例 2：**

```
输入：keyName = ["alice","alice","alice","bob","bob","bob","bob"], keyTime = ["12:01","12:00","18:00","21:00","21:20","21:30","23:00"]
输出：["bob"]
解释："bob" 在一小时内使用了 3 次员工卡（"21:00"，"21:20"，"21:30"）。
```

**示例 3：**

```
输入：keyName = ["john","john","john"], keyTime = ["23:58","23:59","00:01"]
输出：[]
```

**示例 4：**

```
输入：keyName = ["leslie","leslie","leslie","clare","clare","clare","clare"], keyTime = ["13:00","13:20","14:00","18:00","18:51","19:30","19:49"]
输出：["clare","leslie"]
```

 

**提示：**


- ``1 <= keyName.length, keyTime.length <= 10<sup>5</sup>``
- ``keyName.length == keyTime.length``
- ``keyTime`` 格式为 **"HH:MM" **。
- 保证 ``[keyName[i], keyTime[i]]`` 形成的二元对 **互不相同**。
- ``1 <= keyName[i].length <= 10``
- ``keyName[i]`` 只包含小写英文字母。



[LeetCode链接](https://leetcode-cn.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/)

### 思路及代码

题目思路比较清晰，将每个用户的记录时间放到一起，之后比较是否有相邻的三个时间在一个小时之内即可，使用哈希表可以快速实现这一目的。为了判断时间长度，比较容易想到把字符串格式的时间转化为整型。

意外的是，题目中并没有强调记录时间是乱序提供的，初次实现代码时并没有考虑到这点。

```cpp
class Solution {
public:
    int calculateTime(string time){
        return stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3));
    }
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        unordered_map<string,vector<int>> time_map;

        for(int i = 0; i < keyName.size(); i++){
            time_map[keyName[i]].push_back(calculateTime(keyTime[i]));
        }

        // 对每个人的所有时间记录排序，判断相邻三个是否位于同一小时
        vector<string> res;
        // 使用引用格式可以避免数据搬运，提升运行效率
        for(auto &[cur_name, times] : time_map){
            // string cur_name = p.first;
            // vector<int> times = p.second;
            sort(times.begin(), times.end());

            for(int i = 2; i < times.size(); i++){
                if(times[i] - times[i-2] <= 60){
                    res.push_back(cur_name);
                    break;
                }
            }
        }
        sort(res.begin(), res.end());
        return res;
    }
};
```

使用两个哈希表分别存储每个人的记录时间以及相邻两个记录之间的时间间隔，遍历一次即可获得结果的代码，但由于提供的时间记录并不保证有序，所以代码不能通过所有测试用例。

```cpp
class Solution {
public:
    int calculateTime(string time){
        return stoi(time.substr(0, 2)) * 60 + stoi(time.substr(3));
    }
    vector<string> alertNames(vector<string>& keyName, vector<string>& keyTime) {
        set<string> alert_name;
        unordered_map<string,int> last_time;
        unordered_map<string, int> last_diff;


        for(int i = 0; i < keyName.size(); i++){
            int cur_time = calculateTime(keyTime[i]);
            string cur_name = keyName[i];
            cout << cur_time << endl;
            if(last_time.find(cur_name) == last_time.end()){
                last_time[cur_name] = cur_time;
            }
            else{
                int cur_diff = cur_time - last_time[cur_name];
                if(cur_diff < 0){
                    // 超过一天不计算
                    last_diff.erase(cur_name);
                }
                else{
                    if(last_diff.find(cur_name) == last_diff.end()){
                        last_diff[cur_name] = cur_diff;
                    }
                    else{
                        cout << cur_name << ' ' << last_diff[cur_name] << endl;
                        int total_diff = last_diff[cur_name] + cur_diff;
                        if(total_diff <= 60){
                            alert_name.insert(cur_name);
                        }
                        last_diff[cur_name] = cur_diff;
                    }
                }
                last_time[cur_name] = cur_time;
            }
        }

        vector<string> res;
        for(auto s : alert_name){
            res.push_back(s);
        }
        return res;
    }
};
```