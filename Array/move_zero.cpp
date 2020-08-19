#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define V vector<ll>

void moveZeroes(vector<int>& nums) {
        for (int lastNonZeroFoundAt = 0, cur = 0; cur < nums.size(); cur++) {
        if (nums[cur] != 0) {
            swap(nums[lastNonZeroFoundAt++], nums[cur]);
        }
    }
    }

int main(){
	int n;cin>>n;
	V vec(n);
	for(int i=0;i<n;i++)cin>>vec[i];
	moveZeroes(vec,n);
	cout<<vec;
}