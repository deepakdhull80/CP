#include<bits/stdc++.h>
using namespace std;

vector<int> twoSum(vector<int> &numbers, int target)
{
    unordered_map<int, int> hash;
    vector<int> result;
    for (int i = 0; i < numbers.size(); i++) {
        int numberToFind = target - numbers[i];

        if (hash.find(numberToFind) != hash.end()) {
            result.push_back(hash[numberToFind] + 1);
            result.push_back(i + 1);            
            return result;
        }

        hash[numbers[i]] = i;
    }
    return result;
}

int main(){
	int n,target;cin>>n>>target;
	
    vector<int> arr(n,0);
    for(int i=0;i<n;i++)cin>>arr[i];
    vector<int> res=twoSum(arr,target);
	return 0;
}