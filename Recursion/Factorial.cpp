#include <bits/stdc++.h>
using namespace std;


// recursive
int factorial(int n){
	if(n==0){
		return 1;
	}
	return n*(factorial(n-1));
}

// iterative

int iter_factorial(int n){
	int ans= 1;
	for(int i=1;i<=n;i++){
		ans*=i;
	}
	return ans;
}

int main()
{
	int n;
	cout << "Enter the number whose factorial is to be found: \n";
	cin >> n;
	int ans = factorial(n);
	int iter_ans = iter_factorial(n);
	cout << "The factorial by Iterative method: " << iter_ans << "\n";
	cout << "The factorial by Recursive method: " << ans << "\n";
}
