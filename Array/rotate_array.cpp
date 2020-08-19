#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define V vector<int>

void rotate(V &nums,k){
	std::reverse(nums.begin(),nums.end());
        std::reverse(nums.begin(),nums.begin()+k);
        std::reverse(nums.begin()+k,nums.end());
}

int main(){
	int n,k;cin>>n>>k;
	V vec(n);
	for(int i=0;i<n;i++)cin>>vec[i];
	rotate(vec,k);
}