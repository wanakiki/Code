## 355. 设计推特

2020年4月13日

### 题目

设计一个简化版的推特(Twitter)，可以让用户实现发送推文，关注/取消关注其他用户，能够看见关注人（包括自己）的最近十条推文。你的设计需要支持以下的几个功能：

postTweet(userId, tweetId): 创建一条新的推文
getNewsFeed(userId): 检索最近的十条推文。每个推文都必须是由此用户关注的人或者是用户自己发出的。推文必须按照时间顺序由最近的开始排序。
follow(followerId, followeeId): 关注一个用户
unfollow(followerId, followeeId): 取消关注一个用户
示例:
```no
Twitter twitter = new Twitter();

// 用户1发送了一条新推文 (用户id = 1, 推文id = 5).
twitter.postTweet(1, 5);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
twitter.getNewsFeed(1);

// 用户1关注了用户2.
twitter.follow(1, 2);

// 用户2发送了一个新推文 (推文id = 6).
twitter.postTweet(2, 6);

// 用户1的获取推文应当返回一个列表，其中包含两个推文，id分别为 -> [6, 5].
// 推文id6应当在推文id5之前，因为它是在5之后发送的.
twitter.getNewsFeed(1);

// 用户1取消关注了用户2.
twitter.unfollow(1, 2);

// 用户1的获取推文应当返回一个列表，其中包含一个id为5的推文.
// 因为用户1已经不再关注用户2.
twitter.getNewsFeed(1);
```

来源：力扣（LeetCode）  
链接：https://leetcode-cn.com/problems/design-twitter

### 代码

考虑到推文需要频繁的插入，故使用链表进行存储，因为检索推文函数只提取最近的十条，所以推文不能只记录序号，还应记录发布时间，故需要单独设计一个类。

题目并没有告知具体的数据量，而且用户需要快速地查找，所以最好使用哈希表或者足够大的数组来保存用户，我使用了哈希表的方案。

与用户相关的信息有两个，用户推文、用户关注，推文之前已经提到用链表来实现，而考虑到关注取关操作也是进行频繁的插入和删除，所以同样采用了链表方案。

可以把用户封装为类，类中有推文和关注两项内容，把用户id作为key，用户实例作为value维护一个哈希表；也可以对关注和推文分别建立两个哈希表，我使用了后面的方案。至此本题目的基本结构已经定型。

本题目最难的地方在于推文检索的实现，问题可以等价为合并k个有序列表（本题只取前十元素，稍有不同），我参考了[liweiwei1419](https://leetcode-cn.com/problems/design-twitter/solution/ha-xi-biao-lian-biao-you-xian-dui-lie-java-by-liwe/)的解法，使用了堆来获取当前元素。实现起来不是很困难，对于C++来说需要稍微了解一下``priority_queue``的使用方式。

执行时间68ms，击败了50%的用户。

```cpp
class Tweet{
    public:
        int id;
        int time;
        Tweet(int _id, int _time):id(_id),time(_time){}
        // bool operator<(Tweet & b){
        //     return time < b.time;
        // }
        // bool operator>(Tweet& b){
        //     return time < b.time;
        // }
    };

bool operator<(const Tweet&a, const Tweet&b){
        return a.time < b.time;
    }
class Twitter {
private:
    int time;   // 内部时间，判断推文次序
    unordered_map<int, list<Tweet> > userTweets;
    unordered_map<int, list<int> > userFollow;
public:
    
    /** Initialize your data structure here. */
    Twitter() {
        time = 0;
        userTweets.clear();
        userFollow.clear();
    }
    
    /** Compose a new tweet. */
    void postTweet(int userId, int tweetId) {
        userTweets[userId].push_front(Tweet(tweetId, time++));
    } 
    
    /** Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent. */
    vector<int> getNewsFeed(int userId) {
        priority_queue<Tweet> myque;
        for(auto it = userTweets[userId].begin(); it != userTweets[userId].end(); it++){
            myque.push(*it);
        }
        for(auto it = userFollow[userId].begin(); it != userFollow[userId].end(); it++){
            if(*it == userId)   //处理自己关注自己
                continue;
            int count = 0;
            for(auto it2 = userTweets[*it].begin(); it2 != userTweets[*it].end(); it2++){
                if(count == 10)
                    break;
                count++;
                myque.push(*it2);
            }
        }
        int count = 0;
        vector<int> res;
        while(!myque.empty() && count < 10){
            res.push_back(myque.top().id);
            myque.pop();
            count++;
        }
        return res;
    }
    
    /** Follower follows a followee. If the operation is invalid, it should be a no-op. */
    void follow(int followerId, int followeeId) {
        for(auto it = userFollow[followerId].begin(); it != userFollow[followerId].end(); it++){
            if(*it == followeeId){
                return ;    // 避免重复关注
            }
        }
        userFollow[followerId].push_front(followeeId);
    }
    
    /** Follower unfollows a followee. If the operation is invalid, it should be a no-op. */
    void unfollow(int followerId, int followeeId) {
        for(auto it = userFollow[followerId].begin(); it != userFollow[followerId].end(); it++){
            if(*it == followeeId){
                userFollow[followerId].erase(it);
                break;
            }
        }
    }
};

/**
 * Your Twitter object will be instantiated and called as such:
 * Twitter* obj = new Twitter();
 * obj->postTweet(userId,tweetId);
 * vector<int> param_2 = obj->getNewsFeed(userId);
 * obj->follow(followerId,followeeId);
 * obj->unfollow(followerId,followeeId);
 */
```