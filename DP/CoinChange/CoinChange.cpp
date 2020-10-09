// Coin change using DP 
#include<bits/stdc++.h> 
  
using namespace std; 
  
int count( int S[], int m, int n ) 
{ 
    int i, j, x, y; 
  
    int table[n + 1][m]; 
      
    // initialize with 0s
    for (i = 0; i < m; i++) 
        table[0][i] = 1; 
  
    // Fill using Bottom up  
    for (i = 1; i < n + 1; i++) 
    { 
        for (j = 0; j < m; j++) 
        { 
			// Include S[j]
			if (i - S[j] >= 0){
				x = table[i - S[j]][j];
			}else{
				x = 0;
			} 
			// Exclude S[j]
			if(j >= 1){
				y = table[i][j - 1]; 	
			}else{
				y = 0;
			}
            
            // total count 
            table[i][j] = x + y; 
        } 
    } 
    return table[n][m - 1]; 
} 
  
// Driver Code 
int main() 
{ 	
	int coins[100], n, m;
	cout << "Enter total different valued coins \n";
	cin >> m;
	cout << "Enter values of the coins \n";
	for(int i=0; i<m; i++){
		cin >> coins[i];
	}  
    cout << "Enter total Value \n";
	cin >> n; 
    cout << "Total number of ways we can make a change is: " << count(coins, m, n); 
    return 0; 
} 
