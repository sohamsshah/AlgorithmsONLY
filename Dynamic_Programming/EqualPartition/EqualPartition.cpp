#include <stdio.h> 
  
// Returns true if there is a subset of set[] 
// with sun equal to given sum 
bool isSubsetSum(int set[], int n, int sum) 
{ 
    bool subset[n + 1][sum + 1]; 
  
    // If sum is 0, then answer is true 
    for (int i = 0; i <= n; i++) 
        subset[i][0] = true; 
  
    for (int i = 1; i <= sum; i++) 
        subset[0][i] = false; 
  
    for (int i = 1; i <= n; i++) { 
        for (int j = 1; j <= sum; j++) { 
            if (j < set[i - 1]) 
                subset[i][j] = subset[i - 1][j];
            if (j >= set[i - 1]) 
                subset[i][j] = subset[i - 1][j] 
                               || subset[i - 1][j - set[i - 1]]; 
        } 
    } 
  
   //print table 
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
    int set[] = { 856,404,278 }; 
    int n = sizeof(set) / sizeof(set[0]); 
    int sum = 0;
    for(int i = 0; i<n; i++){
    	sum = sum + set[i];
	}
	if(sum%2 != 0){
		printf("No equal partition possible!");
	}
	else{
		if (isSubsetSum(set, n, sum/2) == true) 
        printf("Equal Partition is possible"); 
    else
        printf("No equal partition possible!"); 
    
	}
	return 0; 
    
    
} 
