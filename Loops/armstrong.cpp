#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define V vector<ll>
#define pb(n) push_back(n)
string armstrong(ll n)
{
	ll tmp=n;
	V vec;
	while(n){
		vec.pb(n%10);
		n=n/10;
	}
	ll len=vec.size();
	// cout<<pow(vec[2],len);
	ll res=0;
	for(auto e : vec){
		res+=pow(e,len);
	}
	
	// cout<<res<<endl;
	if(res!=tmp)return "no";
	return "yes";
}

int main()
{
	ll n;
	cin>>n;
	cout<<armstrong(n);
	return 0;
}