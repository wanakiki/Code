#include<iostream>
#include<string>
#include<vector>
#include <algorithm>
#include<sstream>
using namespace std;
int candy(vector<int>& ratings) {
        int len = ratings.size();
        vector<int> res(len,0);
        res[0] = 1;
        for(int i = 1; i < len; i++){
            if(ratings[i] > ratings[i-1])
                res[i] = res[i-1] + 1;
            else
                res[i] = 1;
        }
        int sum = res[len-1];
        for(int j = len-2; j >= 0; j--){
            if(ratings[j] > ratings[j+1] && res[j] <= res[j+1])
                res[j] = res[j+1] +1 ;
                sum += res[j];
        }
        return sum;
    }

int main() {
    string line; 
    /*while (getline(cin, line)) {
        vector<int> ratings;
        for(int i =0;i<line.size();i++){
            if(line[i]!=',')
                ratings.push_back(line[i]-'0');
        }*/
        //cin>>len;
        vector<int> ratings;
        cin>>line;
        for(int i = 0; i < line.size(); i++){
                if('0' <= line[i] && line[i] <='9')
                    ratings.push_back(line[i] - '0');
        }
        int ret =candy(ratings);
        //cout<<"finish"<<endl;
        //string out = to_string(ret);
        cout <<ret;
    return 0;
}

