#include<bits/stdc++.h>
using namespace std;

string longestCommonPrefix(vector<string>& strs) {
        string prefix = "";
        for(int idx=0; strs.size()>0; prefix+=strs[0][idx], idx++)
            for(int i=0; i<strs.size(); i++)
                if(idx >= strs[i].size() ||(i > 0 && strs[i][idx] != strs[i-1][idx]))
                    return prefix;
        return prefix;
    }

int main(){
	
	int n;cin>>n;
	vector<string> strs(n);
	for(int i=0;i<n;i++)cin>>strs[i];
	cout<<longestCommonPrefix(strs);
	return 0;
}