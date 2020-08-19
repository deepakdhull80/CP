#include <bits/stdc++.h>
using namespace std;
#define ll long long
#define V vector<ll>
#define pb(n) push_back(n)


int cal(ll *a, ll *b, ll n, ll m) 
{ 
    int sum[n]; 
  
    int i = n - 1, j = m - 1, k = n - 1; 
  
    int carry = 0, s = 0; 
    while (j >= 0) { 
        s = a[i] + b[j] + carry; 
        sum[k] = (s % 10); 
        carry = s / 10; 
  
        k--; 
        i--; 
        j--; 
    } 
    while (i >= 0) { 
  
        s = a[i] + carry; 
        sum[k] = (s % 10); 
        carry = s / 10; 
  
        i--; 
        k--; 
    } 
  
    int ans = 0; 
  
    if (carry) 
        ans = 10; 
    for (int i = 0; i <= n - 1; i++) { 
        ans += sum[i]; 
        ans *= 10; 
    } 
    return ans / 10; 
}



ll solve(ll *a,ll *b,ll n,ll m){
	ll res=0;
	if(n>=m){
		return cal(a,b,n,m);
	}
	else{
		return cal(b,a,m,n);
	}
}

int main()
{
	ll n,m;
	cin>>n>>m;
	ll a[n],b[m];
	for(int i=0;i<n;i++)
		cin>>a[i];
	for(int i=0;i<m;i++)
		cin>>b[i];
	ll mn=min(n,m);
	cout<<solve(a,b,n,m);
	return 0;
}