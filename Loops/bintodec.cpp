#include<bits/stdc++.h>
using namespace std;
#define ll long long
#define V vector<ll>
#define pb(n) push_back(n)

ll solve(ll n)
{
	// V vec;
	ll i=0;
	ll dec=0;
	while(n){
	// vec.pb(n%10);
	dec+=pow(2,i)*(n%10);
	i++;
	n=n/10;
	// cout<<
	}
	return dec;
	// vec.reverse();
	
}

int main(){
	ll bin;
	cin>>bin;
	cout<<solve(bin);
	return 0;
}