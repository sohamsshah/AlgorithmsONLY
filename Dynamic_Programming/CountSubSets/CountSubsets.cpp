#include <stdio.h> 

  
int countSubsetSum(int set[], int n, int sum) 
{ 
    // The value of subset[i][j] will be true if 
    // there is a subset of set[0..j-1] with sum 
    // equal to i 
    bool subset[n + 1][sum + 1]; 
  
    for (int i = 0; i <= n; i++) 
        subset[i][0] = 1; 
  
    for (int i = 0; i <= sum; i++)
	{
		if(set[0] == j){
			
		}
	 } 
  
    for (int i = 1; i <= n; i++) { 
        for (int j = 1; j <= sum; j++) { 
            int includingitem = 0;
            int excludingitem = 0;
            
            if set[i]
        } 
    } 
  
     for (int i = 0; i <= n; i++) 
     { 
       for (int j = 0; j <= sum; j++) 
          printf ("%4d", subset[i][j]); 
       printf("\n"); 
     }
  
    return subset[n][sum]; 
} 
  
// Driver program to test above function 
int main() 
{ 
    int set[] = {2,3,5,6,8,10}; 
    int sum = 10; 
    int n = sizeof(set) / sizeof(set[0]); 
    if (countSubsetSum(set, n, sum) >= 1) 
        printf("Found a subset with given sum"); 
    else
        printf("No subset with given sum"); 
    return 0; 
} 
